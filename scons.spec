Name:           scons
Version:        1.2.0
Release:        %mkrel 1
Epoch:          1
Summary:        Open Source software construction tool
License:        MIT
Group:          Development/Other
URL:            http://www.scons.org/
Source0:        http://download.sourceforge.net/scons/scons-%{version}.tar.gz
Source1:	scons.macros
Patch0:         scons-1.0.0-qt-handle-missing-moc-files.patch
Requires:       python-%{name} = %{epoch}:%{version}-%{release}
%py_requires -d
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
%py_requires -d

%description -n python-%{name}
The SCons library is required by scons.

%prep
%setup -q
%patch0 -p2

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
    --root=%{buildroot} \
    --record=INSTALLED_FILES \
    --symlink-scons \
    --standard-lib
%{__mkdir_p} %{buildroot}%{_mandir}
%{__mv} %{buildroot}%{_prefix}/man/* %{buildroot}%{_mandir}

# install scons rpm macro helper
install -D %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.d/scons.macros

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt PKG-INFO
%attr(0755,root,root) %{_bindir}/scons
%attr(0755,root,root) %{_bindir}/scons-time
%attr(0755,root,root) %{_bindir}/sconsign
%attr(0755,root,root) %{_bindir}/scons-%{version}
%attr(0755,root,root) %{_bindir}/sconsign-%{version}
%attr(0755,root,root) %{_bindir}/scons-time-%{version}
%{_sysconfdir}/rpm/macros.d/scons.macros
%{_mandir}/man1/scons.1*
%{_mandir}/man1/scons-time.1*
%{_mandir}/man1/sconsign.1*

%files -n python-%{name}
%defattr(0644,root,root,0755)
%{py_puresitedir}/*
