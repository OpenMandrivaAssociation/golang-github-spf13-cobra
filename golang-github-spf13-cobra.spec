# http://github.com/spf13/cobra
%global goipath         github.com/spf13/cobra
%global commit          fe5e611709b0c57fa4a89136deaa8e1d4004d053

%gometa

Name:           %{goname}
Version:        0.0.3
Release:        1%{?dist}
Summary:        A Commander for modern go CLI interactions
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
Cobra is a commander providing a simple interface to create powerful modern
CLI interfaces similar to git & go tools.
In addition to providing an interface, Cobra simultaneously provides
a controller to organize your application code.

Inspired by go, go-Commander, gh and subcommand, Cobra improves on these
by providing fully posix compliant flags (including short & long versions),
nesting commands, and the ability to define your own help and usage
for any or all commands.

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/cpuguy83/go-md2man/md2man)
BuildRequires: golang(github.com/inconshreveable/mousetrap)
BuildRequires: golang(github.com/mitchellh/go-homedir)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/spf13/viper)
BuildRequires: golang(gopkg.in/yaml.v2)

%description devel
Cobra is a commander providing a simple interface to create powerful modern
CLI interfaces similar to git & go tools.
In addition to providing an interface, Cobra simultaneously provides
a controller to organize your application code.

Inspired by go, go-Commander, gh and subcommand, Cobra improves on these
by providing fully posix compliant flags (including short & long versions),
nesting commands, and the ability to define your own help and usage
for any or all commands.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.yaml glide.lock

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE.txt
%doc bash_completions.md README.md

%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.3-1.20181026git1e58aa3
- Bump to commit 1e58aa3361fd650121dceeedc399e7189c05674a

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.0.1-6.git7b2c5ac
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5.git7b2c5ac
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.0.1-4.git7b2c5ac
- Upload glide.lock and glide.yaml files

* Mon Mar 05 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.0.1-3.git7b2c5ac
- Update to spec 3.0

* Fri Mar 02 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.0.1-2
- Autogenerate some parts using the new macros

* Wed Feb 21 2018 Kaushal <kshlmster@gmail.com> - 0.0.1-1
- Update to upstream v0.0.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.git8e91712
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.git8e91712
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.git8e91712
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.19.git8e91712
- Remove cyclic dependency
  related: #1214769

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.git8e91712
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.17.git8e91712
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.16.git8e91712
- Bump to upstream 8e91712f174ced10270cf66615e0a9127e7c4de5
  related: #1214769

* Sat Mar 05 2016 jchaloup <jchaloup@redhat.com> - 0-0.15.git3120920
- Bump to upstream 312092086bed4968099259622145a0c9ae280064
  related: #1214769

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.git8f5946c
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git8f5946c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 jchaloup <jchaloup@redhat.com> - 0-0.12.git8f5946c
- Remove [B]R in comments, they are deleted by the patch
  related: #1214769

* Wed Aug 12 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.11.git8f5946c
- Update spec file to spec-2.0
  related: #1214769

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.git8f5946c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 jchaloup <jchaloup@redhat.com> - 0-0.9.git8f5946c
- Bump to upstream 8f5946caaeeff40a98d67f60c25e89c3525038a3
  related: #1214769

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.8.git3c187e9
- Bump to upstream 3c187e904540cd62f0a197cddd6da02645a7cc5a
  related: #1214769

* Tue Mar 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.git79bd93d
- Bump to upstream 79bd93d369fb73d640179208d4e2b1a748915567
  related: #1085881

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitf8e1ec5
- Bump to upstream f8e1ec56bdd7494d309c69681267859a6bfb7549
  related: #1085881

* Wed Dec 24 2014 jchaloup <jchaloup@redhat.com> - 0-0.5.gitb1e90a7
- Bump to e1e66f7b4e667751cf530ddb6e72b79d6eeb0235
  related: #1085881

* Thu Oct 16 2014 jchaloup <jchaloup@redhat.com> - 0-0.4.gite174a40
- Bump to b1e90a7943957b51bb96a13b44b844475bcf95c0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gite174a40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.git
- correct tarball name

* Fri Apr 04 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git
- Initial package
