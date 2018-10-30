%define	modname	TimeDate
%define modver	1.20

Summary:	%{modname} module for perl (Data_Type_Utilities/Time)
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	18
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/TimeDate/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Simple Time and Date module for perl.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc MANIFEST README ChangeLog
%{perl_vendorlib}/Date
%{perl_vendorlib}/Time
%{_mandir}/man3/*

