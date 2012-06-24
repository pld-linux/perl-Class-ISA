%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	ISA
Summary:	Class::ISA Perl module - report the search path for a class's ISA tree
Summary(cs):	Modul Class::ISA pro Perl
Summary(da):	Perlmodul Class::ISA
Summary(de):	Class::ISA Perl Modul
Summary(es):	M�dulo de Perl Class::ISA
Summary(fr):	Module Perl Class::ISA
Summary(it):	Modulo di Perl Class::ISA
Summary(ja):	Class::ISA Perl �⥸�塼��
Summary(ko):	Class::ISA �� ����
Summary(no):	Perlmodul Class::ISA
Summary(pl):	Modu� perla Class::ISA - zwraca �cie�k� przeszukiwania dla drzewa ISA klasy
Summary(pt_BR):	M�dulo Perl Class::ISA
Summary(pt):	M�dulo de Perl Class::ISA
Summary(ru):	������ ��� Perl Class::ISA
Summary(sv):	Class::ISA Perlmodul
Summary(uk):	������ ��� Perl Class::ISA
Summary(zh_CN):	Class::ISA Perl ģ��
Name:		perl-Class-ISA
Version:	0.32
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
perl Makefile.PL
%{__make}

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
