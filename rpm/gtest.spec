    
Summary:        Google C++ testing framework
Name:           gtest
Version:        1.10.0
Release:        1
# scripts/generator/* are ASL 2.0
License:        BSD and ASL 2.0
URL:            https://github.com/google/googletest
Source0:        https://github.com/google/googletest/archive/release-%{version}/googletest-release-%{version}.tar.gz
# Backports from upstream
# From: https://github.com/google/googletest/pull/2491
Patch0:         gtest-PR2491-Fix-gnu-install-dirs-pkg-config.patch
# From: https://github.com/google/googletest/pull/2556
Patch1:         gtest-PR2556-pkg-config-Remove-pthread-link-flag-from-Cflags.patch
# Fedora-specific patches
## Set libversion for libraries to version of gtest
### Submitted: https://github.com/google/googletest/pull/2755
Patch100:       gtest-1.8.1-libversion.patch
## Add missing pkgconfig requires information to reflect reality
### Submitted: https://github.com/google/googletest/pull/2756
Patch101:       gtest-1.10.0-add-missing-pkgconfig-requires.patch
Patch102:       %{name}-gcc11.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  python3-devel
%description
Framework for writing C++ tests on a variety of platforms (GNU/Linux,
Mac OS X, Windows, Windows CE, and Symbian). Based on the xUnit
architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, various options for running the tests, and XML test report
generation.
 
%package     -n gtest-devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gmock = %{version}-%{release}
%description -n gtest-devel
This package contains development files for %{name}.
 
%package     -n gmock
Summary:        Google C++ Mocking Framework
Requires:       %{name} = %{version}-%{release}
%description -n gmock
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++s
specifics in mind, Google C++ Mocking Framework (or Google Mock for
short) is a library for writing and using C++ mock classes.
 
Google Mock:
 
 o lets you create mock classes trivially using simple macros,
 o supports a rich set of matchers and actions,
 o handles unordered, partially ordered, or completely ordered
   expectations,
 o is extensible by users, and
 o works on Linux, Mac OS X, Windows, Windows Mobile, minGW, and
   Symbian.
 
%package     -n gmock-devel
Summary:        Development files for gmock
Requires:       gmock = %{version}-%{release}
%description -n gmock-devel
This package contains development files for gmock.
 
%prep
%autosetup -p1 -n %{name}-%{version}/%{name}
 
# Set the version correctly
sed -e "s/set(GOOGLETEST_VERSION .*)/set(GOOGLETEST_VERSION %{version})/" -i CMakeLists.txt
 
 
%build
%cmake -DBUILD_SHARED_LIBS=ON \
       -DPYTHON_EXECUTABLE=%{__python3} \
       -Dgtest_build_tests=ON
%cmake_build
%install
%cmake_install
%check
%ctest
%files
%license googletest/LICENSE
%{_libdir}/libgtest.so.%{version}
%{_libdir}/libgtest_main.so.%{version}
 
%files -n gtest-devel
%doc googletest/{CHANGES,CONTRIBUTORS,README.md}
%doc googletest/docs/
%doc googletest/samples
%{_includedir}/gtest/
%{_libdir}/libgtest.so
%{_libdir}/libgtest_main.so
%{_libdir}/cmake/GTest/
%{_libdir}/pkgconfig/gtest.pc
%{_libdir}/pkgconfig/gtest_main.pc
 
%files -n gmock
%license googlemock/LICENSE
%{_libdir}/libgmock.so.%{version}
%{_libdir}/libgmock_main.so.%{version}
 
%files -n gmock-devel
%doc googlemock/{CHANGES,CONTRIBUTORS,README.md}
%doc googlemock/docs/
%{_includedir}/gmock/
%{_libdir}/libgmock.so
%{_libdir}/libgmock_main.so
%{_libdir}/pkgconfig/gmock.pc
%{_libdir}/pkgconfig/gmock_main.pc
