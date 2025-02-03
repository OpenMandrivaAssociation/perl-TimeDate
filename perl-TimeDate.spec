%define	modname	TimeDate

Summary:	%{modname} module for perl (Data_Type_Utilities/Time)
Name:		perl-%{modname}
Version:	2.33
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{modname}
Source0:	https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Simple Time and Date module for perl.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc MANIFEST README ChangeLog
%{perl_vendorlib}/Date
%{perl_vendorlib}/Time
%{_datadir}/perl5/vendor_perl/TimeDate.pm
%doc %{_mandir}/man3/*
