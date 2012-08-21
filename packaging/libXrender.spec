Summary: X.Org X11 libXrender runtime library
Name: libXrender
Version: 0.9.7
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(renderproto)
BuildRequires: libX11-devel

%description
X.Org X11 libXrender runtime library

%package devel
Summary: X.Org X11 libXrender development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libxrender-devel

%description devel
X.Org X11 libXrender development package

%prep
%setup -q

%build
%reconfigure --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
# undo this, we'll add it ourselves in %%doc
rm $RPM_BUILD_ROOT/%{_docdir}/*/libXrender.txt

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libXrender.so.1
%{_libdir}/libXrender.so.1.3.0

%files devel
%defattr(-,root,root,-)
%doc doc/libXrender.txt
%{_includedir}/X11/extensions/Xrender.h
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc
