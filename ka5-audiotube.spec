#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	23.08.5
%define		qt_ver		5.15.10
%define		kf_ver		5.81
%define		kaname		audiotube
Summary:	A client for YouTube Music
Summary(pl.UTF-8):	Klient YouTube Music
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	98514887b61355141f2dde67efd94825
URL:		https://apps.kde.org/audiotube/
BuildRequires:	Qt5Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	futuresql-devel
BuildRequires:	gettext-tools
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kcrash-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kirigami2-devel >= %{kf_ver}
BuildRequires:	kf5-kirigami-addons-devel >= 0.6.0
BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	python3-pybind11
BuildRequires:	python3-yt-dlp
BuildRequires:	python3-ytmusicapi >= 1.0.2
BuildRequires:	qcoro-devel >= 0.9.0
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Concurrent >= %{qt_ver}
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5Qml >= %{qt_ver}
Requires:	Qt5Quick-controls2 >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Sql >= %{qt_ver}
Requires:	Qt5Svg >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-kcrash >= %{kf_ver}
Requires:	kf5-ki18n >= %{kf_ver}
Requires:	kf5-kirigami2 >= %{kf_ver}
Requires:	kf5-kirigami-addons >= 0.6.0
Requires:	kf5-kwindowsystem >= %{kf_ver}
Requires:	python3-yt-dlp
Requires:	python3-ytmusicapi >= 1.0.2
Requires:	qcoro >= 0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AudioTube is a client for YouTube Music.

%description -l pl.UTF-8
AudioTube to klient YouTube Music.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audiotube
%{_desktopdir}/org.kde.audiotube.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.audiotube.svg
%{_datadir}/metainfo/org.kde.audiotube.appdata.xml
