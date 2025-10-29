Name:		    proxmox-backup-client
Version:	    $VERSION
Release:	    1
Summary:	    Proxmox Backup Client
License:	    AGPL-3.0-or-later
URL:		    https://git.proxmox.com/?p=proxmox-backup.git
ExclusiveArch:	x86_64
Source0:	    proxmox-backup.tar.gz
Source1:        pathpatterns.tar.gz
Source2:        proxmox.tar.gz
Source3:        pxar.tar.gz
Source4:        proxmox-fuse.tar.gz

BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: systemd-devel
BuildRequires: libacl-devel
BuildRequires: fuse3-devel
BuildRequires: libuuid-devel

%description
Proxmox Backup Client for Proxmox Backup Server built for RPM based distributions.

%global debug_package %{nil}

%prep
%setup -c
%setup -T -D -a 1
%setup -T -D -a 2
%setup -T -D -a 3
%setup -T -D -a 4
sed -ri "/MAKE_ACCESSORS\(noflush\)/d" proxmox-fuse/src/glue.c
rm -rf proxmox-backup/.cargo
sed -ri "s/^#(proxmox|pbs|pathpatterns|pxar)/\1/" proxmox-backup/Cargo.toml
curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain 1.88.0 -y
. "$HOME/.cargo/env"

%build
cd proxmox-backup
cargo build --release --package proxmox-backup-client --bin proxmox-backup-client --package pxar-bin --bin pxar

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 proxmox-backup/target/release/%{name} %{buildroot}%{_bindir}
install -m 755 proxmox-backup/target/release/pxar %{buildroot}%{_bindir}

%check

%files
%{_bindir}/%{name}
%{_bindir}/pxar

%changelog
* Wed Oct 29 2025 GamerMine <gamermine@dwightstudio.fr>
- Creating package
