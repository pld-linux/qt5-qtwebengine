#
# Conditional build:
%bcond_without	doc	# Documentation

%define		orgname		qtwebengine
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
%define		qtwebchannel_ver	%{version}
Summary:	The Qt5 WebEngine library
Summary(pl.UTF-8):	Biblioteka Qt5 WebEngine
Name:		qt5-%{orgname}
Version:	5.11.1
Release:	0.1
License:	LGPL v3 or GPL v2+ or commercial
Group:		X11/Libraries
Source0:	http://download.qt.io/official_releases/qt/5.11/%{version}/submodules/%{orgname}-everywhere-src-%{version}.tar.xz
# Source0-md5:	75d2ff31addba4ec41981b0f459cc587
Patch0:		remove-compiler-check.patch
URL:		http://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5WebChannel-devel >= %{qtwebchannel_ver}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 WebEngine library.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera bibliotekę Qt5 WebEngine.

%package -n Qt5WebEngine
Summary:	The Qt5 WebEngine library
Summary(pl.UTF-8):	Biblioteka Qt5 WebEngine
Group:		Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}

%description -n Qt5WebEngine
Qt5 WebEngine library provides seamless integration of C++ and QML
applications with HTML/JavaScript clients.

%description -n Qt5WebEngine -l pl.UTF-8
Biblioteka Qt5 WebEngine udostępnia integrację aplikacji C++ i QML z
klientami w HTML-u/JavaScripcie.

%package -n Qt5WebEngine-devel
Summary:	Qt5 WebEngine library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 WebEngine - pliki programistyczne
Group:		Development/Libraries
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Qml-devel >= %{qtdeclarative_ver}
Requires:	Qt5WebEngine = %{version}-%{release}

%description -n Qt5WebEngine-devel
Qt5 WebEngine library - development files.

%description -n Qt5WebEngine-devel -l pl.UTF-8
Biblioteka Qt5 WebEngine - pliki programistyczne.

%package doc
Summary:	Qt5 WebEngine documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 WebEngine w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 WebEngine documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do biblioteki Qt5 WebEngine w formacie HTML.

%package doc-qch
Summary:	Qt5 WebEngine documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 WebEngine w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc-qch
Qt5 WebEngine documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do biblioteki Qt5 WebEngine w formacie QCH.

%package examples
Summary:	Qt5 WebEngine examples
Summary(pl.UTF-8):	Przykłady do biblioteki Qt5 WebEngine
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 WebEngine examples.

%description examples -l pl.UTF-8
Przykłady do biblioteki Qt5 WebEngine.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}
%patch0 -p1

%build
qmake-qt5
%{__make} \
	QMAKE_CXX="g++"
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# Prepare some files list
ifecho() {
	r="$RPM_BUILD_ROOT$2"
	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}
ifecho_tree() {
	ifecho $1 $2
	for f in `find $RPM_BUILD_ROOT$2 -printf "%%P "`; do
		ifecho $1 $2/$f
	done
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/qwebengine
ifecho_tree examples %{_examplesdir}/qt5/webengine

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5WebEngine -p /sbin/ldconfig
%postun	-n Qt5WebEngine -p /sbin/ldconfig

%files -n Qt5WebEngine
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WebEngine.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebEngine.so.5
%dir %{qt5dir}/qml/QtWebEngine
%attr(755,root,root) %{qt5dir}/qml/QtWebEngine/libdeclarative_webengine.so
%{qt5dir}/qml/QtWebEngine/plugins.qmltypes
%{qt5dir}/qml/QtWebEngine/qmldir

%files -n Qt5WebEngine-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WebEngine.so
%{_libdir}/libQt5WebEngine.prl
%{_includedir}/qt5/QtWebEngine
%{_pkgconfigdir}/Qt5WebEngine.pc
%{_libdir}/cmake/Qt5WebEngine
%{qt5dir}/mkspecs/modules/qt_lib_webengine.pri
%{qt5dir}/mkspecs/modules/qt_lib_webengine_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtwebengine

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtwebengine.qch
%endif

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
