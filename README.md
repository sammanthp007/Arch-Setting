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
