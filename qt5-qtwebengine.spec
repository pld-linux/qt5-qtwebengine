#
# Conditional build:
%bcond_without	doc		# documentation
%bcond_without	system_libvpx	# Build with system libvpx

%define		base_version	5.15

%define		orgname		qtwebengine
%define		qtbase_ver		5.15
%define		qtdeclarative_ver	5.15
%define		qtlocation_ver		5.15
%define		qtsvg_ver		5.15
%define		qttools_ver		5.15
%define		qtwebchannel_ver	5.15
Summary:	The Qt5 WebEngine library
Summary(pl.UTF-8):	Biblioteka Qt5 WebEngine
Name:		qt5-%{orgname}
Version:	%{base_version}.15
Release:	1
License:	LGPL v3 or GPL v2 or GPL v3 or commercial
Group:		X11/Libraries
Source0:	qtwebengine-%{version}.tar.xz
# Source0-md5:	fa635b1707607b3eafdc7e099b8cc22c
Patch0:		x32.patch
Patch1:		%{name}-gn-dynamic.patch
Patch2:		0001-avcodec-x86-mathops-clip-constants-used-with-shift-i.patch
URL:		https://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Designer-devel >= %{qttools_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5Positioning-devel >= %{qtlocation_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Svg-devel >= %{qtsvg_ver}
BuildRequires:	Qt5UiTools-devel >= %{qttools_ver}
BuildRequires:	Qt5WebChannel-devel >= %{qtwebchannel_ver}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
BuildRequires:	alsa-lib-devel >= 1.0.10
BuildRequires:	bison
BuildRequires:	dbus-devel
BuildRequires:	expat-devel
# libavcodec libavformat libavutil
BuildRequires:	ffmpeg-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 1:2.4.2
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	glibc-misc >= 6:2.17
BuildRequires:	glibc-devel >= 6:2.17
BuildRequires:	gperf
BuildRequires:	harfbuzz-devel >= 3.0.0
BuildRequires:	harfbuzz-subset-devel >= 3.0.0
# webengine-system-jsoncpp disabled in src/core/config/linux.pri
#BuildRequires:	jsoncpp-devel
BuildRequires:	khrplatform-devel
BuildRequires:	lcms2-devel
BuildRequires:	libdrm-devel
BuildRequires:	libevent-devel
BuildRequires:	libicu-devel >= 65
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.6.0
BuildRequires:	libstdc++-devel >= 6:5
%{?with_system_libvpx:BuildRequires:	libvpx-devel >= 1.8.0}
BuildRequires:	libwebp-devel
BuildRequires:	libxcb-devel
# need icu enabled to be accepted
#BuildRequires:	libxml2-devel >= 2
#BuildRequires:	libxslt-devel
BuildRequires:	minizip-devel
BuildRequires:	ninja
BuildRequires:	nodejs
BuildRequires:	nspr-devel
BuildRequires:	nss-devel >= 3.26
BuildRequires:	opus-devel >= 1.3.1
BuildRequires:	pkgconfig
# checked by qt part, but no longer used by current chromium
#BuildRequires:	poppler-cpp-devel
# webengine-system-protobuf disabled in src/core/config/linux.pri
#BuildRequires:	protobuf-devel
BuildRequires:	pulseaudio-devel >= 0.9.10
BuildRequires:	python >= 1:2.7.5
BuildRequires:	python-modules >= 1:2.7.5
%if %{with doc}
BuildRequires:	qt5-assistant >= 5.15
%endif
BuildRequires:	qt5-build >= 5.15
BuildRequires:	qt5-qmake >= 5.15
BuildRequires:	qt5-qtdoc
BuildRequires:	qt5-qttools
BuildRequires:	re2-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	snappy-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildConflicts:	Qt5WebEngine-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%define		qt5bindir	%(qtpaths-qt5 --binaries-dir)

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
%requires_eq_to	Qt5Core Qt5Core-devel
%requires_ge_to	Qt5Gui Qt5Gui-devel
%requires_ge_to	Qt5Network Qt5Network-devel
%requires_ge_to	Qt5Positioning Qt5Positioning-devel
%requires_ge_to	Qt5Qml Qt5Qml-devel
%requires_ge_to	Qt5Quick Qt5Quick-devel
%requires_ge_to	Qt5WebChannel Qt5WebChannel-devel
Requires:	alsa-lib >= 1.0.10
Requires:	freetype >= 1:2.4.2
Requires:	harfbuzz >= 3.0.0
Requires:	harfbuzz-subset >= 3.0.0
Requires:	libicu >= 65
Requires:	libpng >= 2:1.6.0
%{?with_system_libvpx:Requires:	libvpx >= 1.8.0}
Requires:	nss >= 3.26
Requires:	opus >= 1.3.1
Requires:	pulseaudio-libs >= 0.9.10

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
%requires_ge	Qt5Core-devel
%requires_ge	Qt5Gui-devel
%requires_ge	Qt5Network-devel
%requires_ge	Qt5Positioning-devel
%requires_ge	Qt5PrintSupport-devel
%requires_ge	Qt5Qml-devel
%requires_ge	Qt5Quick-devel
%requires_ge	Qt5WebChannel-devel
Requires:	Qt5WebEngine = %{version}-%{release}
%requires_ge	Qt5Widgets-devel

%description -n Qt5WebEngine-devel
Qt5 WebEngine library - development files.

%description -n Qt5WebEngine-devel -l pl.UTF-8
Biblioteka Qt5 WebEngine - pliki programistyczne.

%package -n Qt5Pdf
Summary:	The Qt5 Pdf library
Summary(pl.UTF-8):	Biblioteka Qt5 Pdf
Group:		Libraries
%requires_eq_to	Qt5Core Qt5Core-devel
%requires_ge_to	Qt5Gui Qt5Gui-devel
%requires_ge_to	Qt5Network Qt5Network-devel
%requires_ge_to	Qt5Qml Qt5Qml-devel
%requires_ge_to	Qt5Quick Qt5Quick-devel
%requires_ge_to	Qt5Widgets Qt5Widgets-devel

%description -n Qt5Pdf
Qt5 Pdf module contains classes and functions for rendering PDF
documents.

%description -n Qt5Pdf -l pl.UTF-8
Moduł Qt5 Pdf zawiera klasy i funkcje do renderowania dokumentów PDF.

%package -n Qt5Pdf-devel
Summary:	Qt5 Pdf library - development files
Summary(pl.UTF-8):	Biblioteka Qt5 Pdf - pliki programistyczne
Group:		Development/Libraries
%requires_ge	Qt5Core-devel
%requires_ge	Qt5Gui-devel
Requires:	Qt5Pdf = %{version}-%{release}
%requires_ge	Qt5Widgets-devel

%description -n Qt5Pdf-devel
Qt5 Pdf library - development files.

%description -n Qt5Pdf-devel -l pl.UTF-8
Biblioteka Qt5 Pdf - pliki programistyczne.

%package -n Qt5Designer-plugin-qwebengineview
Summary:	QWebEngineView plugin for Qt5 Designer
Summary(pl.UTF-8):	Wtyczka QWebEngineView dla Qt5 Designera
Group:		X11/Libraries
%requires_ge_to	Qt5Core Qt5Core-devel
%requires_ge_to	Qt5Gui Qt5Gui-devel
%requires_ge_to	Qt5Designer Qt5Designer-devel
Requires:	Qt5WebEngine = %{version}-%{release}
%requires_ge_to	Qt5Widgets Qt5Widgets-devel

%description -n Qt5Designer-plugin-qwebengineview
QWebEngineView plugin for Qt5 Designer.

%description -n Qt5Designer-plugin-qwebengineview -l pl.UTF-8
Wtyczka QWebEngineView dla Qt5 Designera.

%package doc
Summary:	Qt5 WebEngine documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 WebEngine w formacie HTML
License:	FDL v1.3
Group:		Documentation
%requires_ge_to		qt5-doc-common Qt5Core-devel
BuildArch:	noarch

%description doc
Qt5 WebEngine documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do biblioteki Qt5 WebEngine w formacie HTML.

%package doc-qch
Summary:	Qt5 WebEngine documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 WebEngine w formacie QCH
License:	FDL v1.3
Group:		Documentation
%requires_ge_to		qt5-doc-common Qt5Core-devel
BuildArch:	noarch

%description doc-qch
Qt5 WebEngine documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do biblioteki Qt5 WebEngine w formacie QCH.

%package examples
Summary:	Qt5 WebEngine examples
Summary(pl.UTF-8):	Przykłady do biblioteki Qt5 WebEngine
License:	BSD or commercial
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Qt5 WebEngine examples.

%description examples -l pl.UTF-8
Przykłady do biblioteki Qt5 WebEngine.

%prep
%setup -q -n qtwebengine
%ifarch x32
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1

%{qt5bindir}/syncqt.pl -version %{version}

%build
%ifarch x32
export V8_TARGET_ARCH="x32"
%endif
%{qmake_qt5} CONFIG+=use_gold_linker -- \
	-webengine-ffmpeg \
	-webengine-icu \
	-webengine-opus \
	-webengine-proprietary-codecs \
	-webengine-webp \
	-webengine-webrtc

%{?__jobs:NINJAJOBS="-j %__jobs"} \
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
# misnamed?
%{__rm} $RPM_BUILD_ROOT%{_libdir}/Qt5WebEngineCore.la

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
ifecho_tree examples %{_examplesdir}/qt5/pdf
ifecho_tree examples %{_examplesdir}/qt5/pdfwidgets
ifecho_tree examples %{_examplesdir}/qt5/webengine
ifecho_tree examples %{_examplesdir}/qt5/webenginewidgets

# fixup artificial Qt version dependency
sed -i -e 's/%{version} ${_Qt5WebEngine[^_]*_FIND_VERSION_EXACT}/%{base_version}/' \
	$RPM_BUILD_ROOT%{_libdir}/cmake/Qt5WebEngine*/Qt5WebEngine*Config.cmake

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5WebEngine -p /sbin/ldconfig
%postun	-n Qt5WebEngine -p /sbin/ldconfig

%post	-n Qt5Pdf -p /sbin/ldconfig
%postun	-n Qt5Pdf -p /sbin/ldconfig

%files -n Qt5WebEngine
%defattr(644,root,root,755)
%doc LICENSE.Chromium LICENSE.GPL3-EXCEPT dist/changes-*
# R: Qt5Core Qt5Gui Qt5Network Qt5Qml Qt5Quick Qt5WebChannel Qt5WebEngineCore
%attr(755,root,root) %{_libdir}/libQt5WebEngine.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebEngine.so.5
# R: Qt5Core Qt5Gui Qt5Network Qt5Positioning Qt5Qml Qt5Quick Qt5WebChannel alsa-lib dbus-libs expat fontconfig freetype harfbuzz lcms2 libX11 libXcomposite libXcursor libXdamage libXext libXfixes libXi libXrender libXrandr libXss libavcodec libavformat libavutil libevent libjpeg libicu libpng libvpx libwebp libxcb minizip nspr nss opus re2 snappy zlib
%attr(755,root,root) %{_libdir}/libQt5WebEngineCore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebEngineCore.so.5
# R: Qt5Core Qt5Gui Qt5Network Qt5PrintSupport Qt5Quick Qt5QuickWidgets Qt5WebEngineCore Qt5Widgets
%attr(755,root,root) %{_libdir}/libQt5WebEngineWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5WebEngineWidgets.so.5
%dir %{qt5dir}/qml/QtWebEngine
%{qt5dir}/qml/QtWebEngine/plugins.qmltypes
%{qt5dir}/qml/QtWebEngine/qmldir
%{qt5dir}/qml/QtWebEngine/Controls1Delegates
%{qt5dir}/qml/QtWebEngine/Controls2Delegates
# R: Qt5Core Qt5Qml Qt5Quick Qt5WebEngine Qt5WebEngineCore
%attr(755,root,root) %{qt5dir}/qml/QtWebEngine/libqtwebengineplugin.so
%dir %{_datadir}/qt5/resources
%{_datadir}/qt5/resources/qtwebengine*.pak
%dir %{_datadir}/qt5/translations/qtwebengine_locales
%lang(am) %{_datadir}/qt5/translations/qtwebengine_locales/am.pak
%lang(ar) %{_datadir}/qt5/translations/qtwebengine_locales/ar.pak
%lang(bg) %{_datadir}/qt5/translations/qtwebengine_locales/bg.pak
%lang(bn) %{_datadir}/qt5/translations/qtwebengine_locales/bn.pak
%lang(ca) %{_datadir}/qt5/translations/qtwebengine_locales/ca.pak
%lang(cs) %{_datadir}/qt5/translations/qtwebengine_locales/cs.pak
%lang(da) %{_datadir}/qt5/translations/qtwebengine_locales/da.pak
%lang(de) %{_datadir}/qt5/translations/qtwebengine_locales/de.pak
%lang(el) %{_datadir}/qt5/translations/qtwebengine_locales/el.pak
%lang(en) %{_datadir}/qt5/translations/qtwebengine_locales/en-GB.pak
%lang(en) %{_datadir}/qt5/translations/qtwebengine_locales/en-US.pak
%lang(es) %{_datadir}/qt5/translations/qtwebengine_locales/es.pak
%lang(es_AR,es_BO,es_CL,es_CO,es_CR,es_CU,es_DO,es_EC,es_GT,es_HN,es_MX,es_NI,es_PA,es_PE,es_PR,es_PY,es_SV,es_UY,es_VE) %{_datadir}/qt5/translations/qtwebengine_locales/es-419.pak
%lang(et) %{_datadir}/qt5/translations/qtwebengine_locales/et.pak
%lang(fa) %{_datadir}/qt5/translations/qtwebengine_locales/fa.pak
%lang(fi) %{_datadir}/qt5/translations/qtwebengine_locales/fi.pak
%lang(fil) %{_datadir}/qt5/translations/qtwebengine_locales/fil.pak
%lang(fr) %{_datadir}/qt5/translations/qtwebengine_locales/fr.pak
%lang(gu) %{_datadir}/qt5/translations/qtwebengine_locales/gu.pak
%lang(he) %{_datadir}/qt5/translations/qtwebengine_locales/he.pak
%lang(hi) %{_datadir}/qt5/translations/qtwebengine_locales/hi.pak
%lang(hr) %{_datadir}/qt5/translations/qtwebengine_locales/hr.pak
%lang(hu) %{_datadir}/qt5/translations/qtwebengine_locales/hu.pak
%lang(id) %{_datadir}/qt5/translations/qtwebengine_locales/id.pak
%lang(it) %{_datadir}/qt5/translations/qtwebengine_locales/it.pak
%lang(ja) %{_datadir}/qt5/translations/qtwebengine_locales/ja.pak
%lang(kn) %{_datadir}/qt5/translations/qtwebengine_locales/kn.pak
%lang(ko) %{_datadir}/qt5/translations/qtwebengine_locales/ko.pak
%lang(lt) %{_datadir}/qt5/translations/qtwebengine_locales/lt.pak
%lang(lv) %{_datadir}/qt5/translations/qtwebengine_locales/lv.pak
%lang(ml) %{_datadir}/qt5/translations/qtwebengine_locales/ml.pak
%lang(mr) %{_datadir}/qt5/translations/qtwebengine_locales/mr.pak
%lang(ms) %{_datadir}/qt5/translations/qtwebengine_locales/ms.pak
%lang(nb) %{_datadir}/qt5/translations/qtwebengine_locales/nb.pak
%lang(nl) %{_datadir}/qt5/translations/qtwebengine_locales/nl.pak
%lang(pl) %{_datadir}/qt5/translations/qtwebengine_locales/pl.pak
%lang(pt_BR) %{_datadir}/qt5/translations/qtwebengine_locales/pt-BR.pak
%lang(pt) %{_datadir}/qt5/translations/qtwebengine_locales/pt-PT.pak
%lang(ro) %{_datadir}/qt5/translations/qtwebengine_locales/ro.pak
%lang(ru) %{_datadir}/qt5/translations/qtwebengine_locales/ru.pak
%lang(sk) %{_datadir}/qt5/translations/qtwebengine_locales/sk.pak
%lang(sl) %{_datadir}/qt5/translations/qtwebengine_locales/sl.pak
%lang(sr) %{_datadir}/qt5/translations/qtwebengine_locales/sr.pak
%lang(sv) %{_datadir}/qt5/translations/qtwebengine_locales/sv.pak
%lang(sw) %{_datadir}/qt5/translations/qtwebengine_locales/sw.pak
%lang(ta) %{_datadir}/qt5/translations/qtwebengine_locales/ta.pak
%lang(te) %{_datadir}/qt5/translations/qtwebengine_locales/te.pak
%lang(th) %{_datadir}/qt5/translations/qtwebengine_locales/th.pak
%lang(tr) %{_datadir}/qt5/translations/qtwebengine_locales/tr.pak
%lang(uk) %{_datadir}/qt5/translations/qtwebengine_locales/uk.pak
%lang(vi) %{_datadir}/qt5/translations/qtwebengine_locales/vi.pak
%lang(zh_CN) %{_datadir}/qt5/translations/qtwebengine_locales/zh-CN.pak
%lang(zh_TW) %{_datadir}/qt5/translations/qtwebengine_locales/zh-TW.pak
# R: Qt5Core libevent libicu
%attr(755,root,root)  %{_libdir}/qt5/bin/qwebengine_convert_dict
# R: Qt5Core Qt5WebEngineCore
%attr(755,root,root) %{_libdir}/qt5/libexec/QtWebEngineProcess

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
%{qt5dir}/mkspecs/modules/qt_lib_webengine.pri
%{qt5dir}/mkspecs/modules/qt_lib_webengine_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginecore.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginecore_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginecoreheaders_private.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginewidgets.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_webenginewidgets_private.pri

%files -n Qt5Designer-plugin-qwebengineview
%defattr(644,root,root,755)
# R: Qt5Core Qt5Gui Qt5WebEngineWidgets Qt5Widgets [+Qt5Designer by dir]
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libqwebengineview.so
%{_libdir}/cmake/Qt5Designer/Qt5Designer_QWebEngineViewPlugin.cmake

%files -n Qt5Pdf
%defattr(644,root,root,755)
# R: Qt5Core Qt5Gui Qt5Network freetype libjpeg zlib
%attr(755,root,root) %{_libdir}/libQt5Pdf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Pdf.so.5
# R: Qt5Core Qt5Gui Qt5Pdf Qt5Widgets
%attr(755,root,root) %{_libdir}/libQt5PdfWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5PdfWidgets.so.5
%dir %{qt5dir}/qml/QtQuick/Pdf
%{qt5dir}/qml/QtQuick/Pdf/plugins.qmltypes
%{qt5dir}/qml/QtQuick/Pdf/qmldir
%{qt5dir}/qml/QtQuick/Pdf/qml
# R: Qt5Core Qt5Gui Qt5Pdf Qt5Qml Qt5Quick
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Pdf/libpdfplugin.so
# R: Qt5Core Qt5Gui Qt5Pdf
%attr(755,root,root) %{_libdir}/qt5/plugins/imageformats/libqpdf.so

%files -n Qt5Pdf-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Pdf.so
%attr(755,root,root) %{_libdir}/libQt5PdfWidgets.so
%{_libdir}/libQt5Pdf.prl
%{_libdir}/libQt5PdfWidgets.prl
%{_includedir}/qt5/QtPdf
%{_includedir}/qt5/QtPdfWidgets
%{_pkgconfigdir}/Qt5Pdf.pc
%{_pkgconfigdir}/Qt5PdfWidgets.pc
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QPdfPlugin.cmake
%{_libdir}/cmake/Qt5Pdf
%{_libdir}/cmake/Qt5PdfWidgets
%{qt5dir}/mkspecs/modules/qt_lib_pdf.pri
%{qt5dir}/mkspecs/modules/qt_lib_pdf_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_pdfwidgets.pri
%{qt5dir}/mkspecs/modules/qt_lib_pdfwidgets_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtpdf
%{_docdir}/qt5-doc/qtwebengine

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtpdf.qch
%{_docdir}/qt5-doc/qtwebengine.qch
%endif

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
