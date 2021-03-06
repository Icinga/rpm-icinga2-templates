# Icinga Template Library | (c) 2013-2018 Icinga Development Team | GPLv2+

%define revision 1
%define source_name icinga-template-library

Name:           icinga2-templates
Version:        0.0.0
Release:        %{revision}%{?dist}
Summary:        Icinga Template Library for Icinga 2
Group:          Applications/System
License:        GPLv2+
URL:            https://icinga.com
Source0:        https://github.com/Icinga/%{source_name}/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# TODO: re-enable before offically releasing ITL package
#Conflicts:      icinga2-common < 2.9.0

%description
Icinga Template Library for Icinga 2

%prep
%setup -q

%install
DESTDIR="%{buildroot}" ./install.sh

%files
%defattr(-,root,root)
%{_datadir}/icinga2/include
%doc README.md doc/

%changelog
* Mon Feb 05 2018 Markus Frosch <markus.frosch@icinga.com> 0.0.0-1
- Initial rpm package
