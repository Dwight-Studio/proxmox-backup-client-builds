# proxmox-backup-client-builds
Automatic building of proxmox-backup-client from source for x86_64 RPM based distributions.

# Installation
Installing the proxmox-backup-client package is very easy:
```bash
sudo dnf install dnf-plugins-core # You might already have this
sudo dnf copr enable dwight-studio/proxmox-backup-client
sudo dnf install proxmox-backup-client
```

# Distribution availability
Currently (version 4.0.18), the package is available in the following targets:
> [!WARNING]  
> The following list might be irrelevant. Consider checking on our [Fedora Copr](https://copr.fedorainfracloud.org/coprs/dwight-studio/proxmox-backup-client/builds/) for more details.

## <img src="https://miro.medium.com/v2/1*WzXKURvs7JRfRKtO-xskgw.png" height="20"> Amazon Linux

| Target | State |
|--------|-------|
| Amazon Linux 2023 | ✅ |

---

## <img src="https://www.centos.org/assets/icons/favicon.svg" height="20"> CentOS Stream

| Target | State |
|--------|-------|
| CentOS Stream + EPEL Next 9 | ✅ |
| CentOS Stream 9 | ✅ |

---

## <img src="https://docs.fedoraproject.org/en-US/epel/_images/epel-logo.svg" height="20"> EPEL

| Target | State |
|--------|-------|
| EPEL 10 | ✅ |
| EPEL 9 | ✅ |

---

## <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Fedora_logo.svg" height="20"> Fedora

| Target | State |
|--------|-------|
| Fedora 41 | ✅ |
| Fedora 42 | ✅ |
| Fedora 43 | ✅ |
| Fedora ELN | ✅ |
| Fedora Rawhide | ✅ |

---

## <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/Mageia.svg" height="20"> Mageia

| Target | State |
|--------|-------|
| Mageia 8 | ✅ |
| Mageia 9 | ✅ |
| Mageia Cauldron | ✅ |

---

## <img src="https://www.openeuler.org/favicon.ico" height="20"> openEuler

| Target | State |
|--------|-------|
| openEuler 20.03 | ✅ |
| openEuler 22.03 | ✅ |
| openEuler 24.03 | ✅ |

---

## <img src="https://en.opensuse.org/images/c/cd/Button-colour.png" height="20"> openSUSE

| Target | State |
|--------|-------|
| Leap 15.6 | ❌ |
| Tumbleweed | ✅ |

---

## <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Red_Hat_logo.svg/langfr-1280px-Red_Hat_logo.svg.png" height="20"> RHEL

| Target | State |
|--------|-------|
| RHEL + EPEL 10 | ✅ |
| RHEL 10 | ✅ |
| RHEL 8 | ✅ |
| RHEL 9 | ✅ |

# Disclaimer
This project is **not affiliated** with Proxmox in any way. You are using these builds **AT YOUR OWN RISK**. We are not reponsible of any issue you might encounter.

If you think there is an issue with the build itself, then you can open an issue on this repository.

# License 
The proxmox-backup-client project is under the **AGPL-3.0 license**, so is this repository and this project. You can find a copy of it [here](LICENSE).
