
Name:       libxrender
Summary:    X.Org X11 libXrender runtime library
Version:    0.9.6
Release:    2.5
Group:      Graphics/X Window System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Source1001: packaging/libxrender.manifest 
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(x11)

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Description: %{summary}


%package devel
Summary:    X.Org X11 libXrender development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-filesystem

%description devel
Description: %{summary}


%prep
%setup -q


%build
cp %{SOURCE1001} .
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"
%reconfigure 

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%manifest libxrender.manifest
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libXrender.so.1
%{_libdir}/libXrender.so.1.3.0


%files devel
%manifest libxrender.manifest
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/Xrender.h
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc
%doc %{_datadir}/doc/libXrender/libXrender.txt

