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

Conflicts:      icinga2-common << 2.9.0

%description
Icinga Template Library for Icinga 2

%prep
%setup -q

%build
# noop

%install
DESTDIR="%{buildroot}" ./install.sh

%files
%defattr(-,root,root)
%{_datadir}/icinga2/include

%changelog
* Mon Feb 05 2018 Markus Frosch <markus.frosch@icinga.com> 0.0.0-1
- Initial rpm package
