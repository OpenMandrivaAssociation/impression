%define _empty_manifest_terminate_build 0
Name: impression
Version: 3.5.1
Release: 1
Summary: Impression is a tool to create bootable drives
License: GPL-3.0
Group: System/Configuration/Other
Url: https://gitlab.com/adhami3310/Impression
Source0:  https://gitlab.com/adhami3310/Impression/-/archive/v%{version}/Impression-v%{version}.tar.bz2
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: meson
BuildRequires: rust
BuildRequires: cargo
BuildRequires: pkgconfig(blueprint-compiler)
BuildRequires: python-blueprint-compiler
BuildRequires: python-gi
BuildRequires: python-gobject3
BuildRequires: appstream
BuildRequires: pkgconfig(gtk4) 
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gobject-introspection-1.0)

%description
A tool to write images to portable drives like flash drives or memory
cards.

%prep
%autosetup -n Impression-v%{version} -p 1 -a 1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%{_bindir}/%name
%{_datadir}/applications/io.gitlab.adhami3310.Impression.desktop
%{_datadir}/glib-2.0/schemas/io.gitlab.adhami3310.Impression.gschema.xml
%{_iconsdir}/hicolor/scalable/*
%{_iconsdir}/hicolor/symbolic/*
#{_datadir}/impression/icons/hicolor/scalable*
%{_datadir}/impression/resources.gresource
%{_datadir}/metainfo/io.gitlab.adhami3310.Impression.metainfo.xml
