Summary:	ICE authority file utility
Name:		iceauth
Version:	1.0.10
Release:	1
License:	MIT
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
The iceauth program is used to edit and display the authorization
information used in connecting with ICE.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/iceauth
%doc %{_mandir}/man1/iceauth.1.*
