#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : acpica-unix2
Version  : 20210930
Release  : 60
URL      : https://acpica.org/sites/acpica/files/acpica-unix2-20210930.tar.gz
Source0  : https://acpica.org/sites/acpica/files/acpica-unix2-20210930.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: acpica-unix2-bin = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
Patch1: no-werror.patch

%description
/*
* Miscellaneous instructions for building and using the iASL compiler.
*/
Last update 9 December 2013.

%package bin
Summary: bin components for the acpica-unix2 package.
Group: Binaries

%description bin
bin components for the acpica-unix2 package.


%prep
%setup -q -n acpica-unix2-20210930
cd %{_builddir}/acpica-unix2-20210930
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633035151
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1633035151
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/acpibin
/usr/bin/acpidump
/usr/bin/acpiexamples
/usr/bin/acpiexec
/usr/bin/acpihelp
/usr/bin/acpisrc
/usr/bin/acpixtract
/usr/bin/iasl
