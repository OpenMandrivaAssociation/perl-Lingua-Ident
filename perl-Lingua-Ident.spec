%define	module	Lingua-Ident
%define	name	perl-%{module}
%define	version	1.6
%define	release	%mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Statistical language identification 
License:	GPL or Artistic
Group:		Development/Perl
URL:		    http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Lingua/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module implements a statistical language identifier.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/Lingua
%{_mandir}/*/*


