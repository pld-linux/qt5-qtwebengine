#
# Conditional build:
%bcond_without	doc	# Documentation
%bcond_with	system_libvpx	# Build with system libvpx

%define		orgname		qtwebengine
Summary:	The Qt5 WebEngine library
Summary(pl.UTF-8):	Biblioteka Qt5 WebEngine
Name:		qt5-%{orgname}
Version:	5.12.3
Release:	1
License:	LGPL v3 or GPL v2+ or commercial
Group:		X11/Libraries
Source0:	http://download.qt.io/official_releases/qt/5.12/%{version}/submodules/%{orgname}-everywhere-src-%{version}.tar.xz
# Source0-md5:	9841599435095b16f12870bd48ef5342
Patch0:		remove-compiler-check.patch
Patch1:		x32.patch
URL:		http://www.qt.io/
BuildRequires:	Mesa-khrplatform-devel
BuildRequires:	Qt5Core-devel >= %{version}
BuildRequires:	Qt5Designer-devel >= %{version}
BuildRequires:	Qt5Gui-devel >= %{version}
BuildRequires:	Qt5Network-devel >= %{version}
BuildRequires:	Qt5Positioning-devel >= %{version}
BuildRequires:	Qt5PrintSupport-devel >= %{version}
BuildRequires:	Qt5Qml-devel >= %{version}
BuildRequires:	Qt5Quick-devel >= %{version}
BuildRequires:	Qt5UiTools-devel >= %{version}
BuildRequires:	Qt5WebChannel-devel >= %{version}
BuildRequires:	Qt5WebSockets-devel >= %{version}
BuildRequires:	Qt5Widgets-devel >= %{version}
BuildRequires:	alsa-lib-devel >= 1.0.10
BuildRequires:	bison
BuildRequires:	dbus-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.4.2
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	glibc-misc >= 2.17
BuildRequires:	gperf
BuildRequires:	harfbuzz-devel >= 1.4.2
BuildRequires:	jsoncpp-devel
BuildRequires:	lcms2-devel
BuildRequires:	libdrm-devel
BuildRequires:	libevent-devel
BuildRequires:	libicu-devel >= 53
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.6.0
%{?with_system_libvpx:BuildRequires:	libvpx-devel >= 1.8.0}
BuildRequires:	libwebp-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	minizip-devel
BuildRequires:	ninja
BuildRequires:	nss-devel >= 3.26
BuildRequires:	opus-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-cpp-devel
BuildRequires:	protobuf-devel
BuildRequires:	pulseaudio-devel >= 0.9.10
BuildRequires:	re2-devel
BuildRequires:	snappy-devel
%if %{with doc}
BuildRequires:	qt5-assistant >= %{version}
%endif
BuildRequires:	qt5-build >= %{version}
BuildRequires:	qt5-qmake >= %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildConflicts:	Qt5WebEngine-devel
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
Requires:	Qt5Core >= %{version}
Requires:	Qt5Network >= %{version}
Requires:	Qt5Qml >= %{version}

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
Requires:	Qt5Core-devel >= %{version}
Requires:	Qt5Network-devel >= %{version}
Requires:	Qt5Qml-devel >= %{version}
Requires:	Qt5WebEngine = %{version}-%{release}

%description -n Qt5WebEngine-devel
Qt5 WebEngine library - development files.

%description -n Qt5WebEngine-devel -l pl.UTF-8
Biblioteka Qt5 WebEngine - pliki programistyczne.

%package doc
Summary:	Qt5 WebEngine documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 WebEngine w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{version}
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
Requires:	qt5-doc-common >= %{version}
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
%ifarch x32
%patch1 -p1
%endif
cd ./src/3rdparty/chromium

%build
%ifarch x32
export V8_TARGET_ARCH="x32"
%endif
qmake-qt5 -- \
	-webengine-ffmpeg \
	-webengine-icu
%{__make}
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
ifecho_tree examples %{_examplesdir}/qt5/webengine
ifecho_tree examples %{_examplesdir}/qt5/webenginewidgets

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5WebEngine -p /sbin/ldconfig
%postun	-n Qt5WebEngine -p /sbin/ldconfig

%files -n Qt5WebEngine
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WebEngine.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebEngine.so.5
%attr(755,root,root) %{_libdir}/libQt5WebEngineCore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebEngineCore.so.5
%attr(755,root,root) %{_libdir}/libQt5WebEngineWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebEngineWidgets.so.5
%dir %{qt5dir}/qml/QtWebEngine
%{qt5dir}/qml/QtWebEngine/plugins.qmltypes
%{qt5dir}/qml/QtWebEngine/qmldir
%{qt5dir}/qml/QtWebEngine/Controls1Delegates
%{qt5dir}/qml/QtWebEngine/Controls2Delegates
%attr(755,root,root) %{qt5dir}/qml/QtWebEngine/libqtwebengineplugin.so
%dir %{_datadir}/qt5/resources
%{_datadir}/qt5/resources/qtwebengine*.pak
%attr(755,root,root)  %{_libdir}/qt5/bin/qwebengine_convert_dict
%attr(755,root,root) %{_libdir}/qt5/libexec/QtWebEngineProcess
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libqwebengineview.so

%files -n Qt5WebEngine-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5WebEngine.so
%attr(755,root,root) %{_libdir}/libQt5WebEngineCore.so
%attr(755,root,root) %{_libdir}/libQt5WebEngineWidgets.so
%{_libdir}/libQt5WebEngine.prl
%{_libdir}/libQt5WebEngineCore.prl
%{_libdir}/libQt5WebEngineWidgets.prl
%{_includedir}/qt5/QtWebEngine
%{_includedir}/qt5/QtWebEngineCore
%{_includedir}/qt5/QtWebEngineWidgets
%{_pkgconfigdir}/Qt5WebEngine.pc
%{_pkgconfigdir}/Qt5WebEngineCore.pc
%{_pkgconfigdir}/Qt5WebEngineWidgets.pc
%{_libdir}/cmake/Qt5WebEngine
%{_libdir}/cmake/Qt5WebEngineCore
%{_libdir}/cmake/Qt5WebEngineWidgets
%{_libdir}/cmake/Qt5Designer/Qt5Designer_QWebEngineViewPlugin.cmake
%{qt5dir}/mkspecs/modules/qt_lib_webengine.pri
%{qt5dir}/mkspecs/modules/qt_lib_webengine_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginecore.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginecore_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginecoreheaders_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginewidgets.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginewidgets_private.pri

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
