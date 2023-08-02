Name:           dart
Version:        3.1.0
%define ver %{version}-348.0.dev
Release:        1%{?dist}
Summary:        Dart SDK

License:        BSD
URL:            https://dart.dev/
%define _build_id_links none
ExclusiveArch: %ix86 %arm64 %arm %x86_64 %riscv64 x86_64 riscv64

%ifarch %{x86_64} x86_64
%define dartarch x64
%define dartnum 0
%elifarch %{ix86}
%define dartarch ia32
%define dartnum 1
%elifarch %{arm64} aarch64
%define dartarch arm64
%define dartnum 2
%elifarch %{arm}
%define dartarch arm
%define dartnum 3
%elifarch %{riscv64} riscv64 
%define dartarch riscv64
%define dartnum 4
%endif

%define dartpath %{_usr}/lib/dart-sdk-%{version}-%{dartarch}

%define dartsource() Source%{1}: https://storage.googleapis.com/dart-archive/channels/stable/release/%{ver}/sdk/dartsdk-linux-%{2}-release.zip

%dartsource 0 x64
%dartsource 1 ia32
%dartsource 2 arm64
%dartsource 3 arm
%dartsource 4 riscv64
#Source0:        https://storage.googleapis.com/dart-archive/channels/stable/release/%{ver}/sdk/dartsdk-linux-%{dartarch}-release.zip
Requires(post):    update-alternatives
Requires(postun):  update-alternatives
BuildRequires: unzip
BuildRequires: coreutils
%description
The Dart SDK has the libraries and command-line tools that you need to develop Dart web, command-line, and server apps.

%prep
%autosetup -T -b %{dartnum} -n dart-sdk

%install
mkdir -p '%{buildroot}%{_usr}/lib'
cp -prT ../dart-sdk '%{buildroot}%{dartpath}'

%files
%{dartpath}

%post
%{_sbindir}/update-alternatives --install '%{_usr}/lib/dart-sdk' dart-sdk '%{dartpath}' 25
%{_sbindir}/update-alternatives --install '%{_bindir}/dart' dart '%{dartpath}/bin/dart' 25
%{_sbindir}/update-alternatives --install '%{_bindir}/dartaotruntime' dartaotruntime '%{dartpath}/bin/dartaotruntime' 25 || :

%postun
%{_sbindir}/update-alternatives --remove dartaotruntime '%{dartpath}/bin/dartaotruntime' || : 
%{_sbindir}/update-alternatives --remove dart '%{dartpath}/bin/dart' || : 
%{_sbindir}/update-alternatives --remove dart-sdk '%{dartpath}' || : 

%changelog
* Thu Jul 23 2023 Github Actions <github-actions@users.noreply.github.com> - 3.1.0-1
- update-alternatives postrm and postinst scripts

* Thu Jul 20 2023 Github Actions <github-actions@users.noreply.github.com> - 3.1.0-1
- initial release for opensuse

* Thu Jul 13 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.6-1
- Update Dart SDK

* Thu Jun 15 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.5-1
- Update Dart SDK

* Fri Jun 09 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.4-1
- Update Dart SDK

* Fri Jun 02 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.3-1
- Update Dart SDK

* Thu May 25 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.2-1
- Update Dart SDK

* Thu May 18 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.1-1
- Update Dart SDK

* Wed May 10 2023 Github Actions <github-actions@users.noreply.github.com> - 3.0.0-1
- Update Dart SDK

* Thu Mar 30 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.6-1
- Update Dart SDK

* Thu Mar 23 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.5-1
- Update Dart SDK

* Thu Mar 09 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.4-1
- Update Dart SDK

* Thu Mar 02 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.3-1
- Update Dart SDK

* Thu Feb 09 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.2-1
- Update Dart SDK

* Thu Feb 02 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.1-1
- Update Dart SDK

* Wed Jan 25 2023 Github Actions <github-actions@users.noreply.github.com> - 2.19.0-1
- Update Dart SDK

* Fri Jan 13 2023 Github Actions <github-actions@users.noreply.github.com> - 2.18.7-1
- Update Dart SDK

* Thu Dec 15 2022 Github Actions <github-actions@users.noreply.github.com> - 2.18.6-1
- Update Dart SDK

* Sun Nov 27 2022 Alberto Pedron <albertop2197@gmail.com> - 2.18.5-1
- Initial release
