# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/mmcdole/goxpp
%global goipath         github.com/mmcdole/goxpp
%global commit          2f3784f67354ae364ad309b09bfed2a24a3a06d9

%gometa

%global common_description %{expand:
Go XML Pull Parser.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Go XML Pull Parser

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Oct 04 2021 Adam Thiede <adamj@mailbox.org> - 0-0.1%{?dist}.20211004git2f3784f
- Initial package

