%define		kdeframever	5.19
%define		qtver		5.3.2
%define		kfname		threadweaver

Summary:	Helper for multithreaded programming
Name:		kf5-%{kfname}
Version:	5.19.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	fb9848428899fa10c46121810cf3a022
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
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
%attr(755,root,root) %{_libdir}/libKF5ThreadWeaver.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/ThreadWeaver
%{_includedir}/KF5/threadweaver_version.h
%{_libdir}/cmake/KF5ThreadWeaver
%{_libdir}/libKF5ThreadWeaver.so
%{qt5dir}/mkspecs/modules/qt_ThreadWeaver.pri
