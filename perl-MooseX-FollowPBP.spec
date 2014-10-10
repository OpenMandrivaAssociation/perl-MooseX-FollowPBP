%define upstream_name    MooseX-FollowPBP
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Names accessors in the I<Perl Best Practices> style
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Moose)
BuildArch:	noarch

%description
This module does not provide any methods. Simply loading it changes the
default naming policy for the loading class so that accessors are separated
into get and set methods. The get methods are prefixed with "get_" as the
accessor, while set methods are prefixed with "set_". This is the naming
style recommended by Damian Conway in _Perl Best Practices_.

If you define an attribute with a leading underscore, then both the get and
set method will also have an underscore prefix.

If you explicitly set a "reader" or "writer" name when creating an
attribute, then that attribute's naming scheme is left unchanged.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 657451
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.0-1
+ Revision: 643408
- update to new version 0.05

* Wed Jul 28 2010 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 562137
- rebuild

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 561034
- update to 0.04

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 553962
- update to 0.03

* Mon Jun 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 381877
- adding missing buildrequires:
- import perl-MooseX-FollowPBP


* Mon Jun 01 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

