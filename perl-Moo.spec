#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Moo
Summary:	Moo - Minimalist Object Orientation (with Moose compatibility)
Summary(pl.UTF-8):	Moo - Minimalist Object Orientation (minimalna obiektowość, zgodna z Moose)
Name:		perl-Moo
Version:	2.005004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/H/HA/HAARG/Moo-%{version}.tar.gz
# Source0-md5:	49ecf491b49b9b200e8a5dfd1a42b480
URL:		https://metacpan.org/release/Moo
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-Class-Method-Modifiers >= 2.11
BuildRequires:	perl-Devel-GlobalDestruction >= 0.11
BuildRequires:	perl-Module-Runtime >= 0.014
BuildRequires:	perl-Role-Tiny >= 2.002003
BuildRequires:	perl-Scalar-List-Utils >= 1.00
BuildRequires:	perl-Sub-Quote >= 2.006006
BuildRequires:	perl-Test-Fatal >= 0.003
BuildRequires:	perl-Test-Simple >= 0.94
BuildRequires:	perl-strictures >= 2
%endif
Requires:	perl-Devel-GlobalDestruction >= 0.11
Requires:	perl-Module-Runtime >= 0.014
Requires:	perl-Role-Tiny >= 2.002003
Requires:	perl-Scalar-List-Utils >= 1.00
Requires:	perl-Sub-Quote >= 2.006006
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
documentation.

%description -l pl.UTF-8
Ten moduł to ekstremalnie lekki podzbiór Moose zoptymalizowany pod
kątem szybkiego uruchamiania i "płacenia tylko za to, czego się
używa".

Moduł ten unika także zależności od dowolnych modułów XS, co pozwala
na proste wdrożenia. Nazwa Moo opiera się na idei, że moduł ten
udostępnia prawie - ale nie dokładnie - dwie trzecie Moose.

W przeciwieństwie do Moose, celem modułu nie jest zapewnienie pełnej
zgodności ze składnią Moose, zamiast tego zapewniona jest pełna
interoperacyjność poprzez możliwości inflacji metaklasy, opisane w
dokumentacji.

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
%dir %{perl_vendorlib}/Method
%dir %{perl_vendorlib}/Method/Generate
%{perl_vendorlib}/Method/Generate/Accessor.pm
%{perl_vendorlib}/Method/Generate/BuildAll.pm
%{perl_vendorlib}/Method/Generate/Constructor.pm
%{perl_vendorlib}/Method/Generate/DemolishAll.pm
%{perl_vendorlib}/Moo.pm
%{perl_vendorlib}/Moo
%{perl_vendorlib}/oo.pm
%{_mandir}/man3/Moo.3pm*
%{_mandir}/man3/Moo::Role.3pm*
%{_mandir}/man3/oo.3pm*
