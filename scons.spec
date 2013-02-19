Name:           scons
Version:        2.2.0
Release:        2
Epoch:          1
Summary:        Open Source software construction tool
License:        MIT
Group:          Development/Other
URL:            http://www.scons.org/
Source0:        http://download.sourceforge.net/scons/scons-%{version}.tar.gz
Source1:	scons.macros
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1:2.0.1-3mdv2011.0
+ Revision: 669963
- mass rebuild

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 1:2.0.1-2mdv2011.0
+ Revision: 590140
- rebuild for python 2.7

* Sun Aug 29 2010 Emmanuel Andry <eandry@mandriva.org> 1:2.0.1-1mdv2011.0
+ Revision: 574167
- New version 2.0.1

* Mon Apr 05 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.3.0-1mdv2010.1
+ Revision: 531572
- update to new version 1.3.0
- disable patch 0

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.0-3mdv2010.1
+ Revision: 524072
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:1.2.0-2mdv2010.0
+ Revision: 427063
- rebuild

* Sun Dec 28 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.0-1mdv2009.1
+ Revision: 320094
- new release 1.2.0 (maybe this will fix my weird-ass build error in beid)

* Wed Dec 24 2008 Michael Scherer <misc@mandriva.org> 1:1.1.0-2mdv2009.1
+ Revision: 318437
- rebuild for new python

* Tue Oct 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.1.0-1mdv2009.1
+ Revision: 296192
- update to new version 1.1.0

* Thu Sep 11 2008 Frederik Himpe <fhimpe@mandriva.org> 1:1.0.1-1mdv2009.0
+ Revision: 283842
- Update to new version 1.0.1

* Wed Aug 20 2008 Funda Wang <fwang@mandriva.org> 1:1.0.0-1mdv2009.0
+ Revision: 274115
- switch tarballs
--This line, aind those below, will be ignored--
  AM   SOURCES/scons-1.0.0.tar.gz
  D    SOURCES/scons-src-1.0.0.tar.gz
  M    SPECS/scons.spec
- New version 1.0.0
- rediff patch1

* Sun Aug 10 2008 Funda Wang <fwang@mandriva.org> 1:0.98.5-4mdv2009.0
+ Revision: 270527
- fix typo

* Sun Aug 10 2008 Funda Wang <fwang@mandriva.org> 1:0.98.5-3mdv2009.0
+ Revision: 270347
- add kde3 macros

* Mon Jun 16 2008 Funda Wang <fwang@mandriva.org> 1:0.98.5-2mdv2009.0
+ Revision: 219913
- Add scons macros to ease scons-based packaging

* Mon Jun 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.98.5-1mdv2009.0
+ Revision: 219706
- update to new version 0.98.5
- make use of %%optflags

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 1:0.98.3-1mdv2009.0
+ Revision: 200581
- New version 0.98.3

* Wed Apr 23 2008 Funda Wang <fwang@mandriva.org> 1:0.98.2-1mdv2009.0
+ Revision: 196707
- New version 0.98.2

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.97-2mdv2008.1
+ Revision: 179498
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 29 2007 David Walluck <walluck@mandriva.org> 1:0.97-1mdv2008.0
+ Revision: 32688
- use %%py_requires -d for config/Makefile needed by setup.py install
- install scons to the standard python lib location
- create two packages python-scons (the library) and scons (binaries, manpages, docs)
- 0.97
- add qt patch from Debian
- symlink scons scripts (don't install 2 copies)
- install manpages to the correct directory (%%{_mandir} not %%{_datadir})
- replace uses of  with %%{buildroot}
- explicit %%doc list


* Thu Nov 16 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.96.93-1mdv2007.0
+ Revision: 85024
- Import scons

* Thu Nov 16 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.96.93-1mdv2007.1
- New version 0.96.93

* Tue May 09 2006 Götz Waschk <waschk@mandriva.org> 0.96.92-1mdk
- drop patch
- New release 0.96.92

* Thu May 04 2006 Michael Scherer <misc@mandriva.org> 0.96.91-2mdk
- fix QT detection on i586, as found by GÃ¶tz ( spurious quote in patch 0 )

* Mon Mar 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.96.91-1mdk
- New release 0.96.91
- use mkrel

* Sun Nov 06 2005 Götz Waschk <waschk@mandriva.org> 1:0.96.1-4mdk
- make the previous fix work

* Sun Nov 06 2005 Götz Waschk <waschk@mandriva.org> 0.96.1-3mdk
- another atempt of a fix by the same Gaetan Lehmann

* Sun Nov 06 2005 Götz Waschk <waschk@mandriva.org> 1:0.96.1-2mdk
- lib64 patch by Gaetan Lehmann

* Wed Aug 03 2005 Olivier Blin <oblin@mandriva.com> 1:0.96.1-1mdk
- revert to stable version 0.96.1

* Sat Apr 16 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.96.90-1mdk
- New release 0.96.90

* Wed Aug 25 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.96.1-1mdk
- New release 0.96.1

* Thu Aug 19 2004 Götz Waschk <waschk@linux-mandrake.com> 0.96-1mdk
- source URL
- New release 0.96

* Tue Mar 09 2004 Götz Waschk <waschk@linux-mandrake.com> 0.95-1mdk
- new version

