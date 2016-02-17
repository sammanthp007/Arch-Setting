import logging
import os
import subprocess

from platform import python_version

from libqtile import layout, bar, widget, hook
from libqtile.command import lazy, Client
from libqtile.config import Key, Screen, Group, Drag, Click

alt = 'mod1'
mod = 'mod4'
ctrl = 'control'
shift = 'shift'

terminal = 'urxvt'
#editor = os.getenv('EDITOR', 'subl3')
# editor_cmd = '%s -e %s' % (terminal, editor)
webbrowser = 'chromium'

logger = logging.getLogger('qtile')

keys = [
    # Switch between windows in current stack pane
    # FIXME What is this?
    Key([mod], 'k',
        lazy.layout.down()),
    Key([mod, shift], 'j',
        lazy.layout.up()),

    # Move windows up or down in current stack
    # FIXME What is this?
    Key([mod, ctrl], 'k',
        lazy.layout.shuffle_down()),
    Key([mod, ctrl], 'j',
        lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([alt], 'Tab',
        lazy.layout.next()),

    # Swap panes of split stack
    Key([alt, shift], 'Tab',
        lazy.layout.rotate()),

    # Switch active screen
    # Key([mod], 'Tab',
    #     lazy.next_screen()),

    # Switch layouts
    Key([mod], 'Tab',
        lazy.next_layout()),

    # Restart/Shutdown/Close
    Key([mod, ctrl], 'r',
        lazy.restart()),
    Key([mod, shift], 'q',
        lazy.shutdown()),
    Key([mod, ctrl], 'w',
        lazy.window.kill()),

    # Apps launcher
    Key([mod], 'space',
        lazy.spawncmd()),

    # Apps shortcuts
    Key([mod], 'Return',
        lazy.spawn(terminal)),
]

autostart = {'a': terminal, 's': webbrowser}
groups = [Group(i) for i in "asdfuiop"]
# groups = [Group(i, spawn=autostart.get(i)) for i in "12345"]

# for i in range(len(groups)):
for i in groups:
	# mod1 + letter of group = switch to group
	keys.append(
		Key([mod], i.name, lazy.group[i.name].toscreen())
		)

    # mod1 + shift + letter of group = switch to & move focused window to group
	keys.append(
		Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
		)
    # grp = groups[i].name
    # key = 'F%d' % (i+1)
    # keys.append(Key([mod], key,
    #                 lazy.group[grp].toscreen()))
    # keys.append(Key([mod, shift], key,
    #                 lazy.window.togroup(grp)))

layouts = [
    layout.Max(),
    layout.xmonad.MonadTall(),
    # layout.Stack(num_stacks=2)
]

widget_defaults = dict(
    font='Inconsolata',
    fontsize=12,
    padding=2,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.AGroupBox(),
                widget.Prompt(),
                widget.Spacer(),
                widget.Systray(),
                widget.CPUGraph(),
                widget.BatteryIcon(battery_name='BAT1'),
                widget.Sep(),
                widget.TextBox("Vol."),
                widget.Volume(),
                widget.Sep(),
                widget.Clock(format='%b %-d, %a %H:%M'),
            ],
            24,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Clock(format='%b %-d, %a %H:%M'),
                widget.Spacer(),
                widget.WindowName(),
            ],
            24,
        ),
    ),
]

mouse = [
    Drag([mod], 'Button1',
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], 'Button3',
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], 'Button2',
          lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_wrap = False
floating_layout = layout.Floating()
auto_fullscreen = True

wmname = 'Qtile (Python %s)' % python_version()

@hook.subscribe.current_screen_change
def highlight_screen():
    pass
    #subprocess.call('/home/antoine/.config/qtile/highlight_screen.py')
