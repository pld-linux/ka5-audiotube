#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		audiotube
Summary:	A client for YouTube Music
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e5cf3c85a86dd14bf8cf170ee11b0047
URL:		http://www.kde.org/
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Network-devel >= 5.15.10
BuildRequires:	Qt6Qml-devel >= 5.15.10
BuildRequires:	Qt6Quick-devel >= 5.15.10
BuildRequires:	Qt6Sql-devel >= 5.15.2
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	futuresql-qt6-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.81
BuildRequires:	kf6-kcoreaddons-devel >= 5.81
BuildRequires:	kf6-kcrash-devel >= 5.81
BuildRequires:	kf6-ki18n-devel >= 5.81
BuildRequires:	kf6-kirigami-devel >= 5.81
BuildRequires:	kf6-kwindowsystem-devel >= 5.81
BuildRequires:	kirigami-addons-devel >= 0.6.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	python3-pybind11
BuildRequires:	python3-yt-dlp
BuildRequires:	python3-ytmusicapi >= 1.0.2
BuildRequires:	qcoro-qt6-devel >= 0.9.0
BuildRequires:	qt6-build >= %{qtver}
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
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
