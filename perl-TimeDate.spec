%define	module	TimeDate
%define	name	perl-%{module}
%define	version	1.16
%define	real_version	1.16
%define	release	%mkrel 6

Summary:	%{module} module for perl (Data_Type_Utilities/Time)
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{real_version}.tar.bz2
Url:		http://www.cpan.org
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Requires:	perl
BuildArch:	noarch

%description
Simple Time and Date module for perl.

%prep
%setup -q -n %{module}-%{real_version}

%build
 %{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc MANIFEST README ChangeLog
%{perl_vendorlib}/Date
%{perl_vendorlib}/Time
%{_mandir}/*/*


