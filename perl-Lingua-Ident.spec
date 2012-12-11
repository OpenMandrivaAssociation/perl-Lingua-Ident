%define	upstream_name	 Lingua-Ident
%define upstream_version 1.7

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Statistical language identification 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements a statistical language identifier.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# parallel testing with %make doesn't work
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/Lingua
%{_mandir}/*/*

%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.700.0-1mdv2011.0
+ Revision: 552401
- update to 1.7

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.600.0-1mdv2010.1
+ Revision: 504944
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.6-6mdv2010.0
+ Revision: 430479
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.6-5mdv2009.0
+ Revision: 257536
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.6-4mdv2009.0
+ Revision: 245619
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.6-2mdv2008.1
+ Revision: 133637
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.6-1mdv2007.0
+ Revision: 84473
- new version
- Import perl-Lingua-Ident

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-2mdv2007.0
- Rebuild

* Tue Nov 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdk
- first mdk release

