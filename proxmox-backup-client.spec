Name:           proxmox-backup-client
Version:        $VERSION
Release:        1
Summary:        Proxmox Backup Client
License:        AGPL-3.0-or-later
URL:            https://git.proxmox.com/?p=proxmox-backup.git
Source0:        %{name}-%{version}.tar.gz
BuildArch:      x86_64

%description
Proxmox Backup Client for Proxmox Backup Server built for RPM based distributions.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name} pxar $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_bindir}/pxar

%changelog
* Wed Oct 29 2025 GamerMine <gamermine@dwightstudio.fr>
- Creating package
