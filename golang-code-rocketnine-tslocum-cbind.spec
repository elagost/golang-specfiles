# Generated by go2rpm 1.5.0
%bcond_without check

# https://code.rocketnine.space/tslocum/cbind
%global goipath         code.rocketnine.space/tslocum/cbind
%global forgeurl        https://code.rocketnine.space/tslocum/cbind
%global archiveurl      https://code.rocketnine.space/tslocum/cbind/archive/v%{version}.tar.gz
%global gourl           code.rocketnine.space/tslocum/cbind
Version:                0.1.5

%gometa

%global common_description %{expand:
Key event handling library for tcell }

%global golicenses      LICENSE
%global godocs          CHANGELOG README.md
%global archivename cbind-%{version}

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

License:        MIT
URL:            https://%{goipath}
Source0:        https://code.rocketnine.space/tslocum/cbind/archive/v%{version}.tar.gz

BuildRequires:  golang(github.com/gdamore/tcell/v2)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cbind; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vd                     %{buildroot}%{_datadir}/licenses/golang-code-rocketnine-tslocum-cbind/
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vp %{gobuilddir}/../cbind/LICENSE %{buildroot}%{_datadir}/licenses/golang-code-rocketnine-tslocum-cbind/

%if %{with check}
%check
%gocheck
%endif

%files
%doc %{_datadir}/gocode/src/%{goipath}/cbind/README.md
%license LICENSE
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Oct 04 2021 Adam Thiede <adamj@mailbox.org> - 0.1.5-1%{?dist}
- Initial package

