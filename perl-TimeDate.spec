%define	upstream_name	 TimeDate
%define upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	%{upstream_name} module for perl (Data_Type_Utilities/Time)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/TimeDate/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Simple Time and Date module for perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc MANIFEST README ChangeLog
%{perl_vendorlib}/Date
%{perl_vendorlib}/Time
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-4mdv2012.0
+ Revision: 765777
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-3
+ Revision: 764294
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-2
+ Revision: 667402
- mass rebuild

* Sun Dec 13 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 478055
- update to 1.20

* Sat Sep 26 2009 Jérôme Quelin <jquelin@mandriva.org> 1.190.0-1mdv2010.0
+ Revision: 449367
- update to 1.19

* Sun Sep 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1.170.0-1mdv2010.0
+ Revision: 444845
- update to 1.17

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.0
+ Revision: 408093
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.16-8mdv2009.1
+ Revision: 351708
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.16-7mdv2009.0
+ Revision: 224560
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.16-6mdv2008.1
+ Revision: 180626
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.16-5mdv2007.0
+ Revision: 108427
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-TimeDate

* Tue Jan 18 2005 Abel Cheung <deaddog@mandrake.org> 1.16-4mdk
- rebuild

