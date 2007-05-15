Summary:	-
Summary(pl.UTF-8):	-
Name:		socklibpp
Version:	0.3
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/socklibpp/%{name}-%{version}.tar.gz
# Source0-md5:	f5f7b48e0eb4bf46d2fd0840cb41f03f
URL:		http://socklibpp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
socklib++ is a networking library that provides abstraction for
cross-platform development and high-level design.

%description -l pl.UTF-8

%package devel
Summary:	-
Summary(pl.UTF-8):	-
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel

%description devel -l pl.UTF-8

%package static
Summary:	-
Summary(pl.UTF-8):	-
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static

%description static -l pl.UTF-8

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%doc AUTHORS ChangeLog NEWS README doc/html/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a