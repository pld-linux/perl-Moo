#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Moo
%include	/usr/lib/rpm/macros.perl
Summary:	Moo - Minimalist Object Orientation (with Moose compatibility)
#Summary(pl.UTF-8):
Name:		perl-Moo
Version:	1.007000
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/H/HA/HAARG/Moo-%{version}.tar.gz
# Source0-md5:	45dfb1157721f15d1f80b6514031d4f6
URL:		http://search.cpan.org/dist/Moo/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Method-Modifiers >= 2.11
BuildRequires:	perl-Devel-GlobalDestruction >= 0.11
BuildRequires:	perl-Dist-CheckConflicts >= 0.02
BuildRequires:	perl-Import-Into >= 1.002
BuildRequires:	perl-Module-Runtime >= 0.014
BuildRequires:	perl-Role-Tiny >= 2.000000
BuildRequires:	perl-Test-Fatal >= 0.003
BuildRequires:	perl-strictures >= 1.004003
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an extremely light-weight subset of Moose optimised for
rapid startup and "pay only for what you use".

It also avoids depending on any XS modules to allow simple
deployments. The name Moo is based on the idea that it provides almost
-- but not quite -- two thirds of Moose.

Unlike Mouse this module does not aim at full compatibility with
Moose's surface syntax, preferring instead of provide full
interoperability via the metaclass inflation capabilities described in
/MOO AND MOOSE.

For a full list of the minor differences between Moose and Moo's
surface syntax, see /INCOMPATIBILITIES WITH MOOSE.

# TODO
# %description -l pl.UTF-8

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Moo
%dir %{perl_vendorlib}/Method
%{perl_vendorlib}/Method/*.pm
%dir %{perl_vendorlib}/Method/Generate
%{perl_vendorlib}/Method/Generate/*.pm
%{perl_vendorlib}/Sub/Defer.pm
%{perl_vendorlib}/Sub/Quote.pm
%{_mandir}/man3/*
