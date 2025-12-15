Summary:	Open Source software construction tool
Name:		scons
Version:	4.10.1
Release:	1
License:	MIT
Group:		Development/Other
Url:		https://www.scons.org/
Source0:	https://github.com/SCons/scons/archive/%{version}/scons-%{version}.tar.gz
Source1:	scons.macros
BuildArch:	noarch
Requires:	python-%{name} = %{EVRD}
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(rst2pdf)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sphinx-book-theme)
BuildRequires:	libxml2-utils

%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%package -n python-%{name}
Summary:	SCons library
Group:		Development/Python
Obsoletes:	python2-%{name} < %{EVRD}

%description -n python-%{name}
The SCons library is required by scons.

%prep
%autosetup -p1
python scripts/scons.py

%build
%py_build

%install
%py_install

# install scons rpm macro helper
install -D %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.d/scons.macros

# we don't want these broken and wrongly installed man file
rm -rf %{buildroot}%{_prefix}/scons-time.1
rm -rf %{buildroot}%{_prefix}/scons.1
rm -rf %{buildroot}%{_prefix}/sconsign.1

%files
%{_bindir}/scons
%{_bindir}/scons-configure-cache
%{_bindir}/sconsign
%{_sysconfdir}/rpm/macros.d/scons.macros

%files -n python-%{name}
%{py_puresitedir}/*
