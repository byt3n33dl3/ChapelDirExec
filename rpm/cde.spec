Name: cde
Version: 1.0.0
Release: 1%{?dist}
Summary: SSH bruteforce tool
Group: Applications/Databases
License: MIT
URL: https://github.com/matricali/cde
Source0: https://github.com/matricali/cde/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: libssh-devel
BuildRequires: make
Requires: libssh

%description
Penetration tests on SSH servers using brute force or dictionary attacks.

%prep
%setup -q -n cde-%{version}

%build
make %{?_smp_mflags}

%install
make install DESTDIR="%{buildroot}" PREFIX="" BINDIR="%{_bindir}" MANDIR="%{_mandir}/man1" DATADIR="%{_datadir}/%{name}"
mkdir -p %{buildroot}%{_mandir}/man1
cp docs/man/cde.1 %{buildroot}%{_mandir}/man1/cde.1

%files
%doc README.md
%{!?_licensedir:%global license %doc}
%license LICENSE.txt
%{_bindir}/cde
%{_mandir}/man1/cde.1*

%changelog
* Sat Aug 25 2018 Jorge Matricali <jorgematricali@gmail.com> 0:1.0-0
- Initial RPM build
