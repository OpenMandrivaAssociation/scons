%define name scons
%define version 0.96.93
%define release %mkrel 1

Summary: Open Source software construction tool
Name: %{name}
Version: %{version}
Release: %{release}
Epoch: 1
Source0: http://prdownloads.sourceforge.net/scons/%{name}-%{version}.tar.bz2
License: MIT
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
BuildRequires: libpython-devel
Requires: python
Url: http://www.scons.org/

%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software.  SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax.  SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines.  SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched.  SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %buildroot
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
mkdir -p %buildroot%_datadir/
mv %buildroot%_prefix/man %buildroot%_datadir/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.txt
%{_bindir}/scons
%{_bindir}/sconsign
%{_bindir}/scons-%version
%{_bindir}/sconsign-%version
%{_prefix}/lib/scons-%version/
%{_mandir}/man1/scons.1*
%{_mandir}/man1/sconsign.1*


