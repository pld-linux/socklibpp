Summary:	socklib++ - cross-platform networking library
Summary(pl.UTF-8):	socklib++ - wieloplatformowa biblioteka sieciowa
Name:		socklibpp
Version:	0.3
Release:	1
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
socklib++ to biblioteka sieciowa udostępniająca abstrakcję dla
programowania wieloplatformowego i projektowania wysokopoziomowego.

%package devel
Summary:	Header files for socklib++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki socklib++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for socklib++ library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki socklib++.

%package static
Summary:	Static socklib++ library
Summary(pl.UTF-8):	Statyczna biblioteka socklib++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static socklib++ library.

%description static -l pl.UTF-8
Statyczna biblioteka socklib++.

%prep
%setup -q

%build
%{__libtoolize}
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
%doc AUTHORS ChangeLog NEWS README doc/html/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
