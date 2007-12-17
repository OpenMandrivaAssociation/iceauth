Name: iceauth
Version: 1.0.2
Release: %mkrel 1
Summary: ICE authority file utility
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libice-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The iceauth program is used to edit and display the authorization
information used in connecting with ICE.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/iceauth
%{_mandir}/man1/iceauth.1.*

