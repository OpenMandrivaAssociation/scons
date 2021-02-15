Summary:	Open Source software construction tool
Name:		scons
Version:	4.1.0.post1
Release:	1
License:	MIT
Group:		Development/Other
Url:		http://www.scons.org/
# Looks like source from sourceforge was a bit broken, they not pull latest update with fix for build failures, use instead pypi source
Source0:	http://pypi.io/packages/source/s/SCons/SCons-%{version}.tar.gz
#Source0:	http://download.sourceforge.net/scons/scons-%{version}.tar.gz
Source1:	scons.macros
BuildArch:	noarch
Requires:	python-%{name} = %{EVRD}
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

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
%autosetup -p1 -n SCons-%{version}

%build
%py_build

%install
python setup.py install \
	--root=%{buildroot} \
	--record=INSTALLED_FILES

# install scons rpm macro helper
install -D %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.d/scons.macros

%files
%{_bindir}/scons
%{_bindir}/scons-configure-cache
%{_bindir}/sconsign
%{_sysconfdir}/rpm/macros.d/scons.macros

%files -n python-%{name}
%{py_puresitedir}/*
