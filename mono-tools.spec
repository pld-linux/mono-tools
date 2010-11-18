#
# Conditional build:
%bcond_without	gecko		# don't build gecko html renderer
#
%include	/usr/lib/rpm/macros.mono
Summary:	Mono Tools
Summary(pl.UTF-8):	Narzędzia do mono
Name:		mono-tools
Version:	2.8
Release:	1
License:	GPL v2
Group:		Development/Tools
# latest downloads summary at http://ftp.novell.com/pub/mono/sources-stable/
Source0:	http://ftp.novell.com/pub/mono/sources/mono-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	81d17ee2584acdbc5cfee01adb905e50
Patch0:		%{name}-pwd.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gecko:BuildRequires:	dotnet-gecko-sharp2-devel >= 0.12}
BuildRequires:	dotnet-gnome-desktop-sharp-devel
BuildRequires:	dotnet-gnome-sharp-devel >= 2.16.0
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	dotnet-webkit-sharp-devel >= 0.2-1
BuildRequires:	gettext-devel
BuildRequires:	libgdiplus
BuildRequires:	mono-compat-links
BuildRequires:	mono-csharp
BuildRequires:	mono-devel >= 2.8
BuildRequires:	mono-monodoc >= 2.8
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
Gecko based monodoc HTML renderer.

%description gecko -l pl.UTF-8
Oparty na gecko wyświetlacz HTML-a dla monodoc.

%package webkit
Summary:	WebKit based monodoc HTML renderer
Summary(pl.UTF-8):	Oparty na WebKit wyświetlacz HTML-a dla monodoc
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Provides:	mono-tools-html-renderer

%description webkit
WebKit based monodoc HTML renderer.

%description webkit -l pl.UTF-8
Oparty na WebKit wyświetlacz HTML-a dla monodoc.

%package monowebbrowser
Summary:	Mono.WebBrowser based monodoc HTML renderer
Summary(pl.UTF-8):	Oparty na Mono.WebBrowser wyświetlacz HTML-a dla monodoc
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Provides:	mono-tools-html-renderer

%description monowebbrowser
Mono.WebBrowser based monodoc HTML renderer.

%description monowebbrowser -l pl.UTF-8
Oparty na Mono.WebBrowser wyświetlacz HTML-a dla monodoc.

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
Requires:	monodoc >= 2.6

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

%package mprof-decoder
Summary:	Console decoder for the logging profiler output files
Summary(pl.UTF-8):	Konsolowy dekoder dla plików tworzonych przez logujący profiler
Group:		Development/Tools

%description mprof-decoder
Decodes the contents of a logging profiler output file and prints the
data on standard output.

%description mprof-decoder -l pl.UTF-8
Dekoduje zawartość pliku wynikowego profilera logującego i wypisuje
dane na standardowe wyjście.

%package mprof-heap-viewer
Summary:	GUI viewer for the logging profiler heap snapshots
Summary(pl.UTF-8):	Narzędzie do oglądania migawek sterty profilera logującego
Group:		Development/Tools

%description mprof-heap-viewer
This program decodes the contents of a logging profiler output file
and locates all the heap snapshots inside it. The user can then select
each individual snapshot and decide to load it in memory and explore
its contents.

%description mprof-heap-viewer -l pl.UTF-8
Ten program dekoduje plik wynikowy profilera logującego i lokalizuje
wszystkie znajdujące się w nim migawki sterty. Umożliwia wybranie
dowolnej migawki i załadowanie jej do pamięci w celu obejrzenia
zawartości.

%prep
%setup -q
%patch0 -p1

# as expected by ilcontrast script
%{__sed} -i -e 's,\$(libdir)/ilcontrast,$(prefix)/lib/ilcontrast,' ilcontrast/Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkglibdir=%{_prefix}/lib/mono-tools \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/create-native-map
%attr(755,root,root) %{_bindir}/emveepee
%attr(755,root,root) %{_bindir}/gasnview
%attr(755,root,root) %{_bindir}/gsharp
%attr(755,root,root) %{_bindir}/minvoke
%attr(755,root,root) %{_bindir}/monodoc
%attr(755,root,root) %{_bindir}/mperfmon
%dir %{_prefix}/lib/gsharp
%attr(755,root,root) %{_prefix}/lib/gsharp/gsharp.exe
%{_prefix}/lib/gsharp/gsharp.exe.config
%attr(755,root,root) %{_prefix}/lib/mono/1.0/gasnview.exe
%{_prefix}/lib/create-native-map
%dir %{_prefix}/lib/minvoke
%attr(755,root,root) %{_prefix}/lib/minvoke/minvoke.exe
%dir %{_prefix}/lib/mperfmon
%{_prefix}/lib/mperfmon/config
%attr(755,root,root) %{_prefix}/lib/mperfmon/mperfmon.exe
%dir %{_prefix}/lib/mono-tools
%{_prefix}/lib/mono-tools/Mono.Profiler.Widgets.dll
%attr(755,root,root) %{_prefix}/lib/mono-tools/emveepee.exe
%attr(755,root,root) %{_prefix}/lib/monodoc/browser.exe
%{_prefix}/lib/monodoc/web
%{_desktopdir}/gsharp.desktop
%{_desktopdir}/monodoc.desktop
%{_pixmapsdir}/monodoc.png
%{_pkgconfigdir}/create-native-map.pc
%{_mandir}/man1/create-native-map.1*
%{_mandir}/man1/mperfmon.1*

%if %{with gecko}
%files gecko
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ilcontrast
%{_prefix}/lib/ilcontrast
%{_prefix}/lib/monodoc/GeckoHtmlRender.dll
%{_desktopdir}/ilcontrast.desktop
%{_pixmapsdir}/ilcontrast.png
%endif

%files webkit
%defattr(644,root,root,755)
%{_prefix}/lib/monodoc/WebKitHtmlRender.dll

%files monowebbrowser
%defattr(644,root,root,755)
%{_prefix}/lib/monodoc/MonoWebBrowserHtmlRender.dll

%files gtkhtml
%defattr(644,root,root,755)
%{_prefix}/lib/monodoc/GtkHtmlHtmlRender.dll

%files gendarme
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gendarme
%attr(755,root,root) %{_bindir}/gendarme-wizard
%{_prefix}/lib/gendarme
%{_prefix}/lib/monodoc/sources/Gendarme*
%{_prefix}/lib/monodoc/sources/gendarme*
%{_desktopdir}/gendarme-wizard.desktop
%{_pkgconfigdir}/gendarme-framework.pc
%{_pixmapsdir}/gendarme.svg
%{_mandir}/man1/gendarme.1*
%{_mandir}/man5/gendarme.5*

%files gui-compare
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gui-compare
%{_prefix}/lib/gui-compare

%files mprof-decoder
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mprof-decoder
%{_prefix}/lib/mono-tools/mprof-decoder-library.*
%{_prefix}/lib/mono-tools/mprof-decoder.*
%{_mandir}/man1/mprof-decoder.1*

%files mprof-heap-viewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mprof-heap-viewer
%{_prefix}/lib/mono-tools/mprof-heap-snapshot-explorer.*
%{_prefix}/lib/mono-tools/mprof-heap-viewer.*
%{_mandir}/man1/mprof-heap-viewer.1*
