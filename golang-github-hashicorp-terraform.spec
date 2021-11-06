# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/hashicorp/terraform
%global goipath         github.com/hashicorp/terraform
Version:                1.0.10

%gometa

%global common_description %{expand:
Terraform enables you to safely and predictably create, change, and improve
infrastructure. It is an open source tool that codifies APIs into declarative
configuration files that can be shared amongst team members, treated as code,
edited, reviewed, and versioned.}

%global golicenses      LICENSE
%global godocs          docs BUGPROCESS.md CHANGELOG.md README.md\\\
                        scripts/changelog-links.sh tools/terraform-\\\
                        bundle/README.md docs website/README.md\\\
                        website/guides/core-workflow.html.md\\\
                        website/guides/index.html.md\\\
                        website/guides/terraform-provider-development-\\\
                        program.html.md website/guides/terraform-integration-\\\
                        program.html.md website/intro/index.html.markdown\\\
                        website/intro/use-cases.html.markdown\\\
                        website/intro/vs/boto.html.markdown\\\
                        website/intro/vs/chef-puppet.html.markdown\\\
                        website/intro/vs/cloudformation.html.markdown\\\
                        website/intro/vs/custom.html.markdown\\\
                        website/intro/vs/index.html.markdown website/upgrade-\\\
                        guides/0-10.html.markdown website/upgrade-\\\
                        guides/0-11.html.markdown website/upgrade-\\\
                        guides/0-12.html.markdown website/upgrade-\\\
                        guides/0-14.html.markdown website/upgrade-\\\
                        guides/0-15.html.markdown website/upgrade-\\\
                        guides/0-7.html.markdown website/upgrade-\\\
                        guides/0-8.html.markdown website/upgrade-\\\
                        guides/0-9.html.markdown website/upgrade-\\\
                        guides/1-0.html.markdown website/upgrade-\\\
                        guides/index.html.markdown website/upgrade-\\\
                        guides/0-13.html.markdown

Name:           %{goname}
Release:        1%{?dist}
Summary:        Terraform enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned

# Upstream license specification: BSD-3-Clause and MPL-2.0
License:        BSD and MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(cloud.google.com/go/storage)
BuildRequires:  golang(github.com/agext/levenshtein)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/endpoints)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/sdk/responses)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/services/location)
BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/services/sts)
BuildRequires:  golang(github.com/aliyun/aliyun-oss-go-sdk/oss)
BuildRequires:  golang(github.com/aliyun/aliyun-tablestore-go-sdk/tablestore)
BuildRequires:  golang(github.com/apparentlymart/go-cidr/cidr)
BuildRequires:  golang(github.com/apparentlymart/go-shquot/shquot)
BuildRequires:  golang(github.com/apparentlymart/go-userdirs/userdirs)
BuildRequires:  golang(github.com/apparentlymart/go-versions/versions)
BuildRequires:  golang(github.com/apparentlymart/go-versions/versions/constraints)
BuildRequires:  golang(github.com/armon/circbuf)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/dynamodb)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go/profiles/2017-03-09/resources/mgmt/resources)
BuildRequires:  golang(github.com/Azure/azure-sdk-for-go/services/storage/mgmt/2021-01-01/storage)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/bgentry/speakeasy)
BuildRequires:  golang(github.com/bmatcuk/doublestar)
BuildRequires:  golang(github.com/chzyer/readline)
BuildRequires:  golang(github.com/coreos/pkg/capnslog)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/golang/mock/gomock)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/gophercloud/gophercloud)
BuildRequires:  golang(github.com/gophercloud/gophercloud/openstack/objectstorage/v1/containers)
BuildRequires:  golang(github.com/gophercloud/gophercloud/openstack/objectstorage/v1/objects)
BuildRequires:  golang(github.com/gophercloud/gophercloud/pagination)
BuildRequires:  golang(github.com/gophercloud/utils/terraform/auth)
BuildRequires:  golang(github.com/hashicorp/aws-sdk-go-base)
BuildRequires:  golang(github.com/hashicorp/consul/api)
BuildRequires:  golang(github.com/hashicorp/errwrap)
BuildRequires:  golang(github.com/hashicorp/go-azure-helpers/authentication)
BuildRequires:  golang(github.com/hashicorp/go-azure-helpers/sender)
BuildRequires:  golang(github.com/hashicorp/go-checkpoint)
BuildRequires:  golang(github.com/hashicorp/go-cleanhttp)
BuildRequires:  golang(github.com/hashicorp/go-getter)
BuildRequires:  golang(github.com/hashicorp/go-hclog)
BuildRequires:  golang(github.com/hashicorp/go-multierror)
BuildRequires:  golang(github.com/hashicorp/go-plugin)
BuildRequires:  golang(github.com/hashicorp/go-retryablehttp)
BuildRequires:  golang(github.com/hashicorp/go-tfe)
BuildRequires:  golang(github.com/hashicorp/go-uuid)
BuildRequires:  golang(github.com/hashicorp/go-version)
BuildRequires:  golang(github.com/hashicorp/hcl)
BuildRequires:  golang(github.com/hashicorp/hcl/hcl/ast)
BuildRequires:  golang(github.com/hashicorp/hcl/v2)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/ext/customdecode)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/ext/dynblock)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/ext/tryfunc)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/gohcl)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hcldec)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hcled)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hclparse)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hclsyntax)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hclwrite)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/json)
BuildRequires:  golang(github.com/jmespath/go-jmespath)
BuildRequires:  golang(github.com/joyent/triton-go)
BuildRequires:  golang(github.com/joyent/triton-go/authentication)
BuildRequires:  golang(github.com/joyent/triton-go/errors)
BuildRequires:  golang(github.com/joyent/triton-go/storage)
BuildRequires:  golang(github.com/kardianos/osext)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/lusis/go-artifactory/src/artifactory.v401)
BuildRequires:  golang(github.com/masterzen/winrm)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/mattn/go-shellwords)
BuildRequires:  golang(github.com/mitchellh/cli)
BuildRequires:  golang(github.com/mitchellh/colorstring)
BuildRequires:  golang(github.com/mitchellh/copystructure)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/mitchellh/go-linereader)
BuildRequires:  golang(github.com/mitchellh/go-wordwrap)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/mitchellh/reflectwalk)
BuildRequires:  golang(github.com/packer-community/winrmcp/winrmcp)
BuildRequires:  golang(github.com/pkg/browser)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/posener/complete)
BuildRequires:  golang(github.com/spf13/afero)
BuildRequires:  golang(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common)
BuildRequires:  golang(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile)
BuildRequires:  golang(github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tag/v20180813)
BuildRequires:  golang(github.com/tencentyun/cos-go-sdk-v5)
BuildRequires:  golang(github.com/tombuildsstuff/giovanni/storage/2018-11-09/blob/blobs)
BuildRequires:  golang(github.com/tombuildsstuff/giovanni/storage/2018-11-09/blob/containers)
BuildRequires:  golang(github.com/xanzy/ssh-agent)
BuildRequires:  golang(github.com/xlab/treeprint)
BuildRequires:  golang(github.com/zclconf/go-cty-yaml)
BuildRequires:  golang(github.com/zclconf/go-cty/cty)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/convert)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/function)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/function/stdlib)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/gocty)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/json)
BuildRequires:  golang(github.com/zclconf/go-cty/cty/msgpack)
BuildRequires:  golang(go.etcd.io/etcd/client)
BuildRequires:  golang(go.etcd.io/etcd/clientv3)
BuildRequires:  golang(go.etcd.io/etcd/clientv3/concurrency)
BuildRequires:  golang(go.etcd.io/etcd/pkg/transport)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)
BuildRequires:  golang(golang.org/x/crypto/openpgp)
BuildRequires:  golang(golang.org/x/crypto/openpgp/armor)
BuildRequires:  golang(golang.org/x/crypto/openpgp/errors)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/agent)
BuildRequires:  golang(golang.org/x/crypto/ssh/knownhosts)
BuildRequires:  golang(golang.org/x/mod/sumdb/dirhash)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/idna)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(golang.org/x/text/encoding/ianaindex)
BuildRequires:  golang(google.golang.org/api/impersonate)
BuildRequires:  golang(google.golang.org/api/iterator)
BuildRequires:  golang(google.golang.org/api/option)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  golang(k8s.io/api/coordination/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  golang(k8s.io/client-go/dynamic)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/coordination/v1)
BuildRequires:  golang(k8s.io/client-go/plugin/pkg/client/auth)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api)
BuildRequires:  golang(k8s.io/utils/pointer)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/apparentlymart/go-dump/dump)
BuildRequires:  golang(github.com/dylanmei/winrmtest)
BuildRequires:  golang(github.com/go-test/deep)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(github.com/hashicorp/consul/sdk/testutil)
BuildRequires:  golang(github.com/hashicorp/go-azure-helpers/storage)
BuildRequires:  golang(github.com/hashicorp/hcl/v2/hcltest)
BuildRequires:  golang(github.com/zclconf/go-cty-debug/ctydebug)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/terraform %{goipath}
for cmd in tools/protobuf-compile tools/loggraphdiff; do
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
%doc docs BUGPROCESS.md CHANGELOG.md README.md scripts/changelog-links.sh
%doc tools/terraform-bundle/README.md docs website/README.md
%doc website/guides/core-workflow.html.md website/guides/index.html.md
%doc website/guides/terraform-provider-development-program.html.md
%doc website/guides/terraform-integration-program.html.md
%doc website/intro/index.html.markdown website/intro/use-cases.html.markdown
%doc website/intro/vs/boto.html.markdown
%doc website/intro/vs/chef-puppet.html.markdown
%doc website/intro/vs/cloudformation.html.markdown
%doc website/intro/vs/custom.html.markdown website/intro/vs/index.html.markdown
%doc website/upgrade-guides/0-10.html.markdown
%doc website/upgrade-guides/0-11.html.markdown
%doc website/upgrade-guides/0-12.html.markdown
%doc website/upgrade-guides/0-14.html.markdown
%doc website/upgrade-guides/0-15.html.markdown
%doc website/upgrade-guides/0-7.html.markdown
%doc website/upgrade-guides/0-8.html.markdown
%doc website/upgrade-guides/0-9.html.markdown
%doc website/upgrade-guides/1-0.html.markdown
%doc website/upgrade-guides/index.html.markdown
%doc website/upgrade-guides/0-13.html.markdown
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Nov 06 2021 Adam Thiede <me@adamthiede.com> - 1.0.10-1%{?dist}
- Initial package
