#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	ISA
Summary:	Class::ISA Perl module - report the search path for a class's ISA tree
Summary(pl):	Modu� Perla Class::ISA - zwr�cenie �cie�ki przeszukiwania dla drzewa klasy ISA
Name:		perl-Class-ISA
Version:	0.32
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af2282c351ffb845001cb97ed8ea31fd
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library, Class::ISA, provides functions that return a list (in
order) of names of classes Perl would search to find a method, with
no duplicates.

%description -l pl
Biblioteka Class::ISA udost�pnia funkcje zwracaj�ce (uporz�dkowan�)
list� nazw klas, kt�re Perl powinien przeszuka� w celu znalezienia
zadanej metody (bez duplikat�w).

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
%{_mandir}/man3/*
