Name:		iceauth
Version:	1.0.5
Release:	1
Summary:	ICE authority file utility
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	libice-devel >= 1.0.0
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
The iceauth program is used to edit and display the authorization
information used in connecting with ICE.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/iceauth
%{_mandir}/man1/iceauth.1.*



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 665496
- mass rebuild

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 590416
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 464634
- New version: 1.0.3

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-6mdv2010.0
+ Revision: 425197
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-5mdv2009.1
+ Revision: 351245
- rebuild

* Sun Jul 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdv2009.0
+ Revision: 232144
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 150279
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 24 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.2-1mdv2008.0
+ Revision: 55003
- new upstream version: 1.0.2
- minor configure call cleanup (remove unecessary flags)

* Fri Jul 06 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 48879
- rebuild for 2008


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:26:09 (27462)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

