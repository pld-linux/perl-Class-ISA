%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	ISA
Summary:	Class::ISA Perl module - report the search path for a class's ISA tree
Summary(cs):	Modul Class::ISA pro Perl
Summary(da):	Perlmodul Class::ISA
Summary(de):	Class::ISA Perl Modul
Summary(es):	Módulo de Perl Class::ISA
Summary(fr):	Module Perl Class::ISA
Summary(it):	Modulo di Perl Class::ISA
Summary(ja):	Class::ISA Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Class::ISA ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Class::ISA
Summary(pl):	Modu³ perla Class::ISA - zwraca ¶cie¿kê przeszukiwania dla drzewa ISA klasy
Summary(pt_BR):	Módulo Perl Class::ISA
Summary(pt):	Módulo de Perl Class::ISA
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Class::ISA
Summary(sv):	Class::ISA Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Class::ISA
Summary(zh_CN):	Class::ISA Perl Ä£¿é
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
Biblioteka Class::ISA udostêpnia funkcje zwracaj±ce (uporz±dkowan±)
listê nazw klas, które Perl powinien przeszukaæ w celu znalezienia
zadanej metody (bez duplikatów).

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
