%define upstream_name    MooseX-FollowPBP
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Names accessors in the I<Perl Best Practices> style
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Moose)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


