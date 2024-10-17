%define	modname	TimeDate
%define modver	1.20

Summary:	%{modname} module for perl (Data_Type_Utilities/Time)
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	19
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/TimeDate/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Simple Time and Date module for perl.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc MANIFEST README ChangeLog
%{perl_vendorlib}/Date
%{perl_vendorlib}/Time
%doc %{_mandir}/man3/*
