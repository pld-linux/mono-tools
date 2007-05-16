#
# Conditional build:
%bcond_without	gecko		# don't build gecko html renderer
#
%include	/usr/lib/rpm/macros.mono
Summary:	Mono Tools
Summary(pl.UTF-8):	Narzędzia do mono
Name:		mono-tools
Version:	1.2.4
Release:	1
License:	GPL
Group:		Development/Tools
#Source0Download: http://go-mono.com/sources-stable/
Source0:	http://go-mono.com/sources/mono-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	7d193fea94123a3f30f67bca2873c791
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gecko:BuildRequires:	dotnet-gecko-sharp2-devel >= 0.11}
BuildRequires:	dotnet-gnome-sharp-devel >= 2.15.0
BuildRequires:	mono-compat-links
BuildRequires:	monodoc >= 1.1.16
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	mono-tools-html-renderer
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mono Tools is a collection of development and testing programs and
utilities for use with Mono.

%description -l pl.UTF-8
Mono Tools jest kolekcją rozwojowych i testowych programów oraz
narzędzi do użycia z Mono.

%package gecko
Summary:	Gecko based monodoc HTML renderer
Summary(pl.UTF-8):	Oparty na gecko wyświetlacz HTML-a dla monodoc
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Provides:	mono-tools-html-renderer

%description gecko
Gecko based monodoc HTML renderer. Used instead of GtkHTML based
renderer.

%description gecko -l pl.UTF-8
Oparty na gecko wyświetlacz HTML-a dla monodoc. Jest używany zamiast
wyświetlacza opartego na GtkHTML.

%package gtkhtml
Summary:	GtkHTML based monodoc HTML renderer
Summary(pl.UTF-8):	Oparty na GtkHTML wyświetlacz HTML-a dla monodoc
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Provides:	mono-tools-html-renderer

%description gtkhtml
GtkHTML based monodoc HTML renderer.

%description gtkhtml -l pl.UTF-8
Oparty na GtkHTML wyświetlacz HTML-a dla monodoc.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	assemblydir=%{_libdir}/create-native-map \
	monodocdir=%{_libdir}/monodoc \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/create-native-map
%attr(755,root,root) %{_bindir}/gasnview
%attr(755,root,root) %{_bindir}/gnunit
%attr(755,root,root) %{_bindir}/gnunit2
%attr(755,root,root) %{_bindir}/ilcontrast
%{_prefix}/lib/mono/1.0/*
%{_prefix}/lib/mono/2.0/*
%{_libdir}/create-native-map
%{_libdir}/ilcontrast
%{_libdir}/monodoc/browser.exe
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/create-native-map.1*

%if %{with gecko}
%files gecko
%defattr(644,root,root,755)
%{_libdir}/monodoc/GeckoHtmlRender.dll
%endif

%files gtkhtml
%defattr(644,root,root,755)
%{_libdir}/monodoc/GtkHtmlHtmlRender.dll
