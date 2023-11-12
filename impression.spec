Name: impression
Version: 3.0.1
Release: 1
Summary: Impression is a tool to create bootable drives
License: GPL-3.0
Group: System/Configuration/Other
Url: https://gitlab.com/adhami3310/Impression
Source0:  https://gitlab.com/adhami3310/Impression/-/archive/v%{version}/Impression-v%{version}.tar.bz2
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires: meson
BuildRequires: rust
BuildRequires: blueprint-compiler
BuildRequires: /usr/bin/appstreamcli
BuildRequires: pkgconfig(gtk4) 
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(dbus-1)

%description
A tool to write images to portable drives like flash drives or memory
cards.

%prep
%autosetup -p 1 -a 1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
#%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc PRESS* README*
