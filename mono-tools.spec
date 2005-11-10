%include	/usr/lib/rpm/macros.mono
Summary:	Mono Tools
Summary(pl):	Narzêdzia do mono
Name:		mono-tools
Version:	1.1.10
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://go-mono.com/sources/mono-tools/%{name}-%{version}.tar.gz
# Source0-md5:	1d0cce057b2c425ff5fb4ffc2f68d5f4
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gecko-sharp-devel = 0.6
BuildRequires:	dotnet-gtk-sharp-gnome-devel
BuildRequires:	mono-compat-links
BuildRequires:	monodoc >= 1.0.7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	mono-tools-html-renderer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mono Tools is a collection of development and testing programs and
utilities for use with Mono.

%description -l pl
Mono Tools jest kolekcj± rozwojowych i testowych programów oraz
narzêdzi do u¿ycia z Mono.

%package gecko
Summary:	Gecko based monodoc HTML renderer
Summary(pl):	Oparty na gecko wy¶wietlacz HTML-a dla monodoc
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Provides:	mono-tools-html-renderer

%description gecko
Gecko based monodoc HTML renderer. Used instead of Gtk.HTML based
renderer.

%description gecko -l pl
Oparty na gecko wy¶wietlacz HTML-a dla monodoc. Jest u¿ywany zamiast
wy¶wietlacza opartego na Gtk.HTML.

%package gtkhtml
Summary:	GtkHTML based monodoc HTML renderer
Summary(pl):	Oparty na GtkHTML wy¶wietlacz HTML-a dla monodoc
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Provides:	mono-tools-html-renderer

%description gtkhtml
GtkHTML based monodoc HTML renderer. Used instead of Gtk.HTML based
renderer.

%description gtkhtml -l pl
Oparty na GtkHTML wy¶wietlacz HTML-a dla monodoc. Jest u¿ywany zamiast
wy¶wietlacza opartego na Gtk.HTML.

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
%attr(755,root,root) %{_bindir}/gasnview
%attr(755,root,root) %{_bindir}/gnunit
%attr(755,root,root) %{_bindir}/gnunit2
%{_prefix}/lib/mono/1.0/*
%{_prefix}/lib/mono/2.0/*
%{_prefix}/lib/monodoc/browser.exe
%{_desktopdir}/*
%{_pixmapsdir}/*

%files gecko
%defattr(644,root,root,755)
%{_prefix}/lib/monodoc/GeckoHtmlRender.dll

%files gtkhtml
%defattr(644,root,root,755)
%{_prefix}/lib/monodoc/GtkHtmlHtmlRender.dll
