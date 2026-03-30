#
# spec file for package uget
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           uget
Version:        2.2.5
Release:        0
Summary:        Download Manager with a GTK+ user interface
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            http://github.com/qr243vbi/uget
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  (update-desktop-files or	desktop-file-utils)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  filesystem
Requires:       aria2

%description
Uget is a download manager written with GTK+. It supports
pause and resume, and the ability to classify download, with every
category having an independent configuration.

%package lang 
Summary: Translations for package %{name} 
Group: System/Localization 
Requires: %{name} = %{version}  
Provides: %{name}-lang-all = %{version} 
BuildArch: noarch 

%description lang 
Provides translations for the "%{name}" package.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS README COPYING
%{_bindir}/%{name}-gtk
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}-icon.*
%{_datadir}/icons/hicolor/*/apps/%{name}-tray-*
%dir %{_datadir}/pixmaps/%{name}/
%{_datadir}/pixmaps/%{name}/logo.png
%dir %{_datadir}/sounds/%{name}/
%{_datadir}/sounds/%{name}/notification.wav

%files lang
%{_datadir}/locale/**/*

%changelog
