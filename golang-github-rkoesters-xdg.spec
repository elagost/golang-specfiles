# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/rkoesters/xdg
%global goipath         github.com/rkoesters/xdg
Version:                0.0.1

%gometa

%global common_description %{expand:
FreeDesktop.org (xdg) Specs implemented in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        FreeDesktop.org (xdg) Specs implemented in Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
mkdir -p $HOME/.local/share/Trash/files
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Oct 04 2021 Adam Thiede <adamj@mailbox.org> - 0.0.1-1%{?dist}
- Initial package

