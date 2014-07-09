# TODO:
# - dir /usr/include/KF5 not packaged
# /usr/lib/qt5/qml/org/kde not packaged
# /usr/lib/qt5/plugins/kf5
# /usr/share/kf5

%define         _state          stable
%define		orgname		threadweaver

Summary:	Helper for multithreaded programming
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	23426ad8caacb0e494d870c546a3783c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
ThreadWeaver is a helper for multithreaded programming. It uses a
job-based interface to queue tasks and execute them in an efficient
way.

You simply divide the workload into jobs, state the dependencies
between the jobs and ThreadWeaver will work out the most efficient way
of dividing the work between threads within a set of resource limits.

See the information on [use cases](@ref usecases) and [why
multithreading can help](@ref multithreading), as well as the usage
section below, for more detailed information.

%package devel
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %ghost %{_libdir}/libKF5ThreadWeaver.so.5
%attr(755,root,root) %{_libdir}/libKF5ThreadWeaver.so.5.0.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/ThreadWeaver
%{_includedir}/KF5/threadweaver_version.h
%{_libdir}/cmake/KF5ThreadWeaver
%{_libdir}/libKF5ThreadWeaver.so
%{qt5dir}/mkspecs/modules/qt_ThreadWeaver.pri
