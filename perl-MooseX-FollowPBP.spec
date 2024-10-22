%define upstream_name    MooseX-FollowPBP

Name:		perl-%{upstream_name}
Version:	0.05
Release:	1

Summary:	Names accessors in the I<Perl Best Practices> style
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/MooseX::FollowPBP
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{version}.tar.gz

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
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
