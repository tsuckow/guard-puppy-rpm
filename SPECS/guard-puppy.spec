Name:		guard-puppy
Version:	0.4
Release:	1%{?dist}
Summary:	Qt4 firewall configuration utility based on GuardDog

Group:		Applications/Internet
License:	GPL
URL:		https://github.com/robopanda333/guard-puppy
Source0:	guard-puppy.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	qt-devel
Requires:	qt

%description


%prep
%setup


%build
qmake-qt4
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
/usr/bin/guard-puppy


%changelog

