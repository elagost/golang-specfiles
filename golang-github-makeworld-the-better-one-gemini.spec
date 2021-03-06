# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/makeworld-the-better-one/go-gemini
%global goipath         github.com/makeworld-the-better-one/go-gemini
Version:                0.11.1

%gometa

%global common_description %{expand:
Client and server library for the Gemini protocol, in Go.}

%global golicenses      LICENSE LICENSE-GO
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Client and server library for the Gemini protocol, in Go

# Upstream license specification: ISC and BSD-3-Clause
License:        ISC and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/idna)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
%endif

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
* Mon Oct 04 2021 Adam Thiede <adamj@mailbox.org> - 0.11.1-1%{?dist}
- Initial package

