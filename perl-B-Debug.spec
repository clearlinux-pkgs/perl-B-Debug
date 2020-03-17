#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-B-Debug
Version  : 1.26
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Debug-1.26.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Debug-1.26.tar.gz
Summary  : 'print debug info about ops'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-B-Debug-license = %{version}-%{release}
Requires: perl-B-Debug-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
B::Debug - Walk Perl syntax tree, printing debug info about ops
SYNOPSIS
perl -MO=Debug foo.pl
perl -MO=Debug,-exec foo.pl

%package dev
Summary: dev components for the perl-B-Debug package.
Group: Development
Provides: perl-B-Debug-devel = %{version}-%{release}
Requires: perl-B-Debug = %{version}-%{release}

%description dev
dev components for the perl-B-Debug package.


%package license
Summary: license components for the perl-B-Debug package.
Group: Default

%description license
license components for the perl-B-Debug package.


%package perl
Summary: perl components for the perl-B-Debug package.
Group: Default
Requires: perl-B-Debug = %{version}-%{release}

%description perl
perl components for the perl-B-Debug package.


%prep
%setup -q -n B-Debug-1.26
cd %{_builddir}/B-Debug-1.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-B-Debug
cp %{_builddir}/B-Debug-1.26/Copying %{buildroot}/usr/share/package-licenses/perl-B-Debug/1fa102688dd2d79dbf4cf269aabd2e5482ab7734
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/B::Debug.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-B-Debug/1fa102688dd2d79dbf4cf269aabd2e5482ab7734

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/B/Debug.pm
