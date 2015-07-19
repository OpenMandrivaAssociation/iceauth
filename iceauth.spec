Summary:	ICE authority file utility
Name:		iceauth
Version:	1.0.7
Release:	2
License:	MIT
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
The iceauth program is used to edit and display the authorization
information used in connecting with ICE.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/iceauth
%{_mandir}/man1/iceauth.1.*
