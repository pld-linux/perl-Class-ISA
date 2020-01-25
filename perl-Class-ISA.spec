#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Class
%define		pnam	ISA
Summary:	Class::ISA Perl module - report the search path for a class's ISA tree
Summary(pl.UTF-8):	Moduł Perla Class::ISA - zwrócenie ścieżki przeszukiwania dla drzewa klasy ISA
Name:		perl-Class-ISA
Version:	0.36
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a2ad203c8dc87d6c9de16215d00af47
URL:		http://search.cpan.org/dist/Class-ISA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library, Class::ISA, provides functions that return a list (in
order) of names of classes Perl would search to find a method, with no
duplicates.

%description -l pl.UTF-8
Biblioteka Class::ISA udostępnia funkcje zwracające (uporządkowaną)
listę nazw klas, które Perl powinien przeszukać w celu znalezienia
zadanej metody (bez duplikatów).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_vendorlib}/Class/ISA.pm
%{_mandir}/man3/Class::ISA.3pm*
