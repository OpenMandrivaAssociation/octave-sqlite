%global octpkg sqlite

Summary:	Native SQLite interface for GNU Octave
Name:		octave-sqlite
Version:	0.0.2
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/sqlite/
Url:		https://github.com/gnu-octave/octave-sqlite/
Source0:	https://github.com/gnu-octave/octave-sqlite/releases/download/v%{version}/octave-sqlite-%{version}.tar.gz

BuildRequires:  octave-devel >= 6.0.0
BuildRequires:  pkgconfig(sqlite3)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Basic Octave implementation of the sqlite toolkit.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

