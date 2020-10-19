Name: jolla-hw-adaptation-pinetab
Summary: Jolla HW Adaptation pinetab
Version: 0.0.1
Release: 1
License: BSD-3-Clause
Source: %{name}-%{version}.tar.gz

Requires: qt5-plugin-generic-evdev

# Graphics (mesa)
Requires: mesa-dri-drivers
Requires: mesa-libEGL
Requires: mesa-libGLESv2
Requires: mesa-libgbm
Requires: mesa-libglapi
Requires: wayland-egl
Requires: qt5-plugin-platform-eglfs

# Splash screen
Requires: plymouth-lite
Requires: plymouth-lite-theme-default

# Bluetooth tools
Requires: bluez5-tools
#Requires: bluetooth-rfkill-event-hciattach

# Vibra
Requires: ngfd-plugin-native-vibrator
Requires: qt5-feedback-haptics-native-vibrator

# Sensors
#Requires: hybris-libsensorfw-qt5

#PA needs work
#Requires: pulseaudio-modules-droid
#Requires: pulseaudio-modules-droid-glue

# for audio recording to work:
Requires: qt5-qtmultimedia-plugin-mediaservice-gstmediacapture

# These need to be per-device due to differing backends (fbdev, eglfs, hwc, ..?)
Requires: qt5-qtwayland-wayland_egl

# Add GStreamer v1.0 as standard
Requires: gstreamer1.0
Requires: gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-base
Requires: gstreamer1.0-plugins-bad
Requires: nemo-gstreamer1.0-interfaces
#Requires: gstreamer1.0-droid

# This is needed for notification LEDs
Requires: mce-plugin-libhybris-nondroid

## USB mode controller
## Enables mode selector upon plugging USB cable:
Requires: usb-moded
#Requires: usb-moded-defaults-android
#Requires: usb-moded-developer-mode-android

Requires: rfkill

# enable device lock and allow to select untrusted software
Requires: jolla-devicelock-plugin-encsfa

# For GPS
Requires: gpsd
Requires: geoclue

# For mounting SD card automatically
Requires: sd-utils

# sound
Requires: alsa-utils

# Cameras
Requires: v4l-utils

# Bluetooth binaries
Requires: realtek-bt-firmware

Requires: kernel-adaptation-pine64
Requires: droid-config-pinetab-sailfish
Requires: droid-config-pinetab-pulseaudio-settings
Requires: droid-config-pinetab-policy-settings
Requires: droid-config-pinetab-preinit-plugin
Requires: droid-config-pinetab-bluez5
Requires: droid-hal-version-pinetab
#Requires: droid-config-donebeevil-flashing

%description
Meta package to install packages for PineTab HW Adaptation
%files
 
