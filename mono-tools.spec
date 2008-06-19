#
# Conditional build:
%bcond_without	gecko		# don't build gecko html renderer
#
%include	/usr/lib/rpm/macros.mono
Summary:	Mono Tools
Summary(pl.UTF-8):	Narzędzia do mono
Name:		mono-tools
Version:	1.9
Release:	3
License:	GPL v2
Group:		Development/Tools
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/mono-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	f00eb74bd0f467f81fad3ab62e215e1a
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gecko:BuildRequires:	dotnet-gecko-sharp2-devel >= 0.12}
BuildRequires:	dotnet-gnome-sharp-devel >= 2.16.0
BuildRequires:	dotnet-gnome-desktop-sharp-devel
BuildRequires:	mono-compat-links
BuildRequires:	monodoc >= 1.2.6
BuildRequires:	mono-jscript
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sed >= 4.0
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

%package gendarme
Summary:	A tool to find problems in .NET applications and libraries
Summary(pl.UTF-8):	Narzędzie znajdujące problemy w aplikacjach i bibliotekach .NET
Group:		Development/Tools

%description gendarme
Gendarme is a extensible rule-based tool to find problems in .NET
applications and libraries. Gendarme inspects programs and libraries
that contain code in ECMA CIL format (Mono and .NET) and looks for
common problems with the code, problems that compiler do not typically
check or have not historically checked.

%description gendarme -l pl.UTF-8
Gendarme to rozszerzalne narzędzie oparte o regułki, znajdujące
problemy w aplikacjach i bibliotekach .NET. Gendarme przeprowadza
inspekcję programów i bibliotek w formacie ECMA CIL (Mono i .NET)
szukając typowych problemów, których często kompilator nie sprawdza,
lub tych które nie były kiedyś sprawdzane.

%package gui-compare
Summary:	Compares API changes between different assemblies
Summary(pl.UTF-8):	Porównuje zmiany API między różnymi assembly
Group:		Development/Tools

%description gui-compare
Compares API changes between different assemblies.

%description gui-compare -l pl.UTF-8
Porównuje zmiany API między różnymi assembly.

%prep
%setup -q

# as expected by ilcontrast script
sed -i -e 's,\$(libdir)/ilcontrast,$(prefix)/lib/ilcontrast,' ilcontrast/Makefile.am

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
%{_prefix}/lib/mono/1.0/gasnview.exe
%{_prefix}/lib/mono/1.0/gnunit.exe
%{_prefix}/lib/mono/2.0/gnunit2.exe
%{_prefix}/lib/create-native-map
%{_libdir}/monodoc/browser.exe
%{_desktopdir}/monodoc.desktop
%{_pixmapsdir}/monodoc.png
%{_pkgconfigdir}/create-native-map.pc
%{_mandir}/man1/create-native-map.1*

%if %{with gecko}
%files gecko
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ilcontrast
%{_prefix}/lib/ilcontrast
%{_libdir}/monodoc/GeckoHtmlRender.dll
%{_desktopdir}/ilcontrast.desktop
%{_pixmapsdir}/ilcontrast.png
%endif

%files gtkhtml
%defattr(644,root,root,755)
%{_libdir}/monodoc/GtkHtmlHtmlRender.dll

%files gendarme
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gendarme
%{_prefix}/lib/gendarme
%{_pkgconfigdir}/gendarme-framework.pc
%{_mandir}/man1/gendarme.1*

%files gui-compare
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gui-compare
%{_prefix}/lib/gui-compare
