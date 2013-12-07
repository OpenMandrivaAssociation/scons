Summary:        Open Source software construction tool
Name:           scons
Epoch:          1
Version:        2.3.0
Release:        5
License:        MIT
Group:          Development/Other
Url:            http://www.scons.org/
Source0:        http://download.sourceforge.net/scons/scons-%{version}.tar.gz
Source1:	scons.macros
BuildArch:      noarch
Requires:       python-%{name} = %{epoch}:%{version}-%{release}
BuildRequires:	python-devel

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
Summary:        SCons library
Group:          Development/Python

%description -n python-%{name}
The SCons library is required by scons.

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
python setup.py install \
	--root=%{buildroot} \
	--record=INSTALLED_FILES \
	--symlink-scons \
	--standard-lib
mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}%{_prefix}/man/* %{buildroot}%{_mandir}

# install scons rpm macro helper
install -D %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.d/scons.macros

%files
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt PKG-INFO
%{_bindir}/scons
%{_bindir}/scons-time
%{_bindir}/sconsign
%{_bindir}/scons-%{version}
%{_bindir}/sconsign-%{version}
%{_bindir}/scons-time-%{version}
%{_sysconfdir}/rpm/macros.d/scons.macros
%{_mandir}/man1/scons.1*
%{_mandir}/man1/scons-time.1*
%{_mandir}/man1/sconsign.1*

%files -n python-%{name}
%{py_puresitedir}/*

