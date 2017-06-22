# My ArchLinux-Setting
My preferred setting for Arch Linux (Qtile)

### Disable touchpad on the fly
```
synclient MaxTapTime=0
synclient MaxTapMove=0 
```

### Permanently disable touchpad
edit in  /etc/X11/xorg.conf.d/50-synaptics.conf
```
Option "MaxTapTime" "0"
Option "MaxTapMove" "0"
```

### Disable TouchScreen on the fly
```
xinput -l
xinput disable 10
```
### If using Qtile as your desktop environment:
My configuration can be found [here](./config.py)

## Troubleshooting (Get started)
1. USB stick with arch linux live
2. Mount your computer in the arch in the usb
```
mount /dev/sdax /mnt
```
3. Enable internet in the arch in USB
```
wpa_supplicant -B -i interface -c <(wpa_passphrase MYSSID passphrase)
```
4. Check if you have internet
```
ping google.com
ping 8.8.8.8
```
5. Mount the needed fs of your live usb arch to your computer
```
mount -o bind /sys /mnt/sys
mount -o bind /proc /mnt/proc
mount -o bind /dev /mnt/dev
```
6. Reset the network in order for the route/dns stuff to be setup.
```
dhclient eth0
# or
dhcpcd
```
7. Chroot
```
chroot /mnt
```
8. Check internet connection
```
ping 8.8.8.8
ping google.com
```
> If success on 8.8.8.8 but failure on google.com, then check your dns. For that check your `/etc/resolv.conf` file. or if not check this [link](https://wiki.archlinux.org/index.php/Network_configuration)


### If you ever delete `/etc/ssl/certs/ca-certificates.cert` then
```
pacman -S ca-certificates-utils
```
