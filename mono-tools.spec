Summary:	Mono Tools
Summary(pl):	Narzêdzia do mono
Name:		mono-tools
Version:	1.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://go-mono.com/sources/mono-tools/%{name}-%{version}.tar.gz
# Source0-md5:	9e7db3d6c56226f237b34cb0cd8763d3
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp-devel
BuildRequires:	mono
BuildRequires:	mono-compat-links
BuildRequires:	monodoc
BuildRequires:	pkgconfig
Requires:	monodoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mono Tools is a collection of development and testing programs and
utilities for use with Mono.

%description -l pl
Mono Tools jest kolekcj± rozwojowych i testowych programów oraz
narzêdzi do u¿ycia z Mono.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_libdir}/mono
%{_libdir}/monodoc/browser.exe
%{_desktopdir}/*
%{_pixmapsdir}/*
