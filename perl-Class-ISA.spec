#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	ISA
Summary:	Class::ISA Perl module - report the search path for a class's ISA tree
Summary(pl):	Modu³ perla Class::ISA - zwraca ¶cie¿kê przeszukiwania dla drzewa ISA klasy
Name:		perl-Class-ISA
Version:	0.32
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library, Class::ISA, provides functions that return a list (in
order) of names of classes Perl would search to find a method, with
no duplicates.

%description -l pl
Biblioteka Class::ISA udostêpnia funkcje zwracaj±ce (uporz±dkowan±)
listê nazw klas, które Perl powinien przeszukaæ w celu znalezienia
zadanej metody (bez duplikatów).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_sitelib}/Class/ISA.pm
%{_mandir}/man3/*
