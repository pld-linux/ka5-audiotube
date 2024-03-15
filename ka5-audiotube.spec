#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.4
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		audiotube
Summary:	A client for YouTube Music
Name:		ka5-%{kaname}
Version:	23.08.4
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	30cacb33bb9681fcd0687709bc95c938
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Network-devel >= 5.15.10
BuildRequires:	Qt5Qml-devel >= 5.15.10
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel >= 5.15.10
BuildRequires:	Qt5Sql-devel >= 5.15.2
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	futuresql-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.81
BuildRequires:	kf5-kcoreaddons-devel >= 5.81
BuildRequires:	kf5-kcrash-devel >= 5.81
BuildRequires:	kf5-ki18n-devel >= 5.81
BuildRequires:	kf5-kirigami2-devel >= 5.81
BuildRequires:	kf5-kwindowsystem-devel >= 5.81
BuildRequires:	kirigami-addons-devel >= 0.6.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	python3-pybind11
BuildRequires:	python3-yt-dlp
BuildRequires:	python3-ytmusicapi >= 1.0.2
BuildRequires:	qcoro-devel >= 0.9.0
BuildRequires:	qcoro-devel >= 0.9.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AudioTube is a client for YouTube Music.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,zh_CN}

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audiotube
%{_desktopdir}/org.kde.audiotube.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.audiotube.svg
%{_datadir}/metainfo/org.kde.audiotube.appdata.xml
