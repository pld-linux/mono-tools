%include	/usr/lib/rpm/macros.mono
Summary:	Mono Tools
Summary(pl):	Narzêdzia do mono
Name:		mono-tools
Version:	1.1.9
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://go-mono.com/sources/mono-tools/%{name}-%{version}.tar.gz
# Source0-md5:	52797a026f99a6e6fb235dc36240e797
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gecko-sharp-devel = 0.6
BuildRequires:	dotnet-gtk-sharp-gnome-devel
BuildRequires:	mono-compat-links
BuildRequires:	monodoc >= 1.0.7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
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

%description gecko
Gecko based monodoc HTML renderer. Used instead of Gtk.HTML based
renderer.

%description gecko -l pl
Oparty na gecko wy¶wietlacz HTML-a dla monodoc. Jest u¿ywany zamiast
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

%post
echo "Please wait, generating index..."
/usr/bin/monodoc --make-index >/dev/null 2>/dev/null || :
/usr/bin/monodoc --make-search-index >/dev/null 2>/dev/null || :

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
