%package -n patterns-sailfish-device-configuration-pinetab
Summary: Sailfish Configuration Pinetab

Requires: patterns-sailfish-device-configuration-common-pinetab
Requires: patterns-sailfish-device-adaptation-pinetab
Requires: patterns-sailfish-applications
Requires: patterns-sailfish-ui

# Jolla Store Items
Requires: patterns-sailfish-consumer-generic
Requires: patterns-sailfish-store-applications

Requires: sailfish-content-graphics-z1.0
Requires: jolla-settings-accounts-extensions-3rd-party-all

# For Mozilla location services (online)
Requires: geoclue-provider-mlsdb

# Sailfish OS CSD tool for hardware testing
Requires: csd

# KMod required for kmod-static-nodes.service 
Requires: kmod

#Debug tools
Recommends: vi
Recommends: strace
Recommends: gdb
Recommends: mce-tools

#Sailfish porter tools
Recommends: jolla-developer-mode
Recommends: sailfishsilica-qt5-demos
Recommends: busybox-static
Recommends: net-tools
Recommends: openssh-clients
Recommends: openssh-server
Recommends: vim-enhanced
Recommends: zypper
Recommends: strace
Recommends: jolla-rnd-device

#Chum
Recommends: sailfishos-chum-gui

%description -n patterns-sailfish-device-configuration-pinetab
Pattern with packages for pinetab configurations

%files -n patterns-sailfish-device-configuration-pinetab
