from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord
from libqtile import layout
from libqtile.config import Match
from libqtile.config import Drag, Click
from libqtile import bar, widget
from libqtile.config import Screen

import subprocess

from libqtile import hook

import os 
import subprocess

mod = "mod1"
terminal = "alacritty"


## --------------------  Keys ----------------------------------------
# ----------------------------------------------------------------------
keys = [
    # Switch between windows
    Key([mod], "h", lazy.group.prev_window(), desc="Move focus to left"),
    Key([mod], "l", lazy.group.next_window(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Key([mod], "Return", lazy.spawn("tmux.sh"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("dmenu_run -fn 'Roboto Mono-16' -l 10 -nb '#333333' -nf '#f5f5f5' -sf '#268bd2' -sb '#ffffff'"),
        desc="Spawn a command using a prompt widget"),

    # setting up redshift
    Key([mod, "control"], "n", lazy.spawn("xgamma -bgamma 0.4")),
    Key([mod, "control"], "d", lazy.spawn("xgamma -bgamma 1.0")),

    #    setting up volume control key bindings
    Key([mod, "shift"], "Right", lazy.spawn("amixer -c 0 sset 'Speaker' 2%+")),
    Key([mod, "shift"], "Left", lazy.spawn("amixer -c 0 sset 'Speaker' 2%-")),
    Key([mod, "shift"], "Up", lazy.spawn("amixer -c 0 sset 'Speaker' toggle")),
    Key([mod, "shift"], "Down", lazy.spawn(
        "amixer -c 0 sset 'Speaker' toggle")),

    # Navigate to the workspace on the left
    Key([mod], "Left", lazy.screen.prev_group()),
    # Navigate to the workspace on the right
    Key([mod], "Right", lazy.screen.next_group()),

    # scratchpad for cmus, thunderbird, kitty...
    Key([mod], "s", lazy.group['scratchpad'].dropdown_toggle('music')),
    Key([mod], "e", lazy.group['scratchpad'].dropdown_toggle('email')),
    Key([mod], "q", lazy.group['scratchpad'].dropdown_toggle('quickie')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('spotify')),

    # running the vm
    Key([mod], "v", lazy.spawn("sudo /home/reda/.config/qtile/scripts/win10.sh")),

    # Qutebrowser mode
    KeyChord([mod], "b", [
        Key([], "b", lazy.spawn("qutebrowser --set zoom.default 125")),
        Key([], "d", lazy.spawn("/home/reda/.config/qtile/scripts/dmenu/meriam-dict.sh")),
        Key([], "p", lazy.spawn("/home/reda/.config/qtile/scripts/dmenu/piracy.sh")),
        Key([], "y", lazy.spawn("/home/reda/.config/qtile/scripts/dmenu/youtube.sh")),
        Key([], "r", lazy.spawn("qutebrowser --set zoom.default 125  --target window https://www.reddit.com/")),
        Key([], "c", lazy.spawn(
            "qutebrowser  --target window --set zoom.default 125 https://chat.openai.com/")),
        Key([], "g", lazy.spawn(
            "qutebrowser  --target window --set zoom.default 125 https://gemini.google.com/app")),
        Key([], "m", lazy.spawn("qutebrowser --target window --set zoom.default 125 http://m.inpt.ac.ma/my/ ':open -t https://gemini.google.com/app;;open -t https://chat.openai.com/;;open -t https://web.whatsapp.com/'")),
    ],
        mode=True,
        name="browser mode"
    ),

    # Software mode
    KeyChord([mod],"a", [
        Key([], "f", lazy.spawn("kitty -e vifm")),
        Key([], "l", lazy.spawn("libreoffice")),
        ], 
             mode=True,
             name="software mode",
            ),

]
# MOVE/RESIZE FLOATING WINDOW
for key, x, y in [
        ("Left", -10, 0),
        ("Right", 10, 0),
        ("Up", 0, -10),
        ("Down", 0, 10)]:
    keys.append(Key([mod, "control"], key, lazy.window.move_floating(x, y)))
    keys.append(Key([mod, "shift"], key, lazy.window.resize_floating(x, y)))

## --------------------  Groups ----------------------------------------
# ----------------------------------------------------------------------

scratch_dict = {'height': 0.8,
                'width': 0.6,
                'x': 0.2,
                'y': 0.1,
                'on_focus_lost_hide': False,
                'warp_pointer': False}

scratchpads = [ScratchPad('scratchpad',
                          [
                              DropDown('music',
                                       'alacritty -e cmus',
                                       **scratch_dict),
                              DropDown(
                                  'email',
                                  'alacritty -e neomutt',
                                  **scratch_dict),
                              DropDown(
                                  'spotify',
                                  'spotify',
                                  **scratch_dict),
                              DropDown(
                                  'quickie',
                                  'alacritty --command tmux attach',
                                  **scratch_dict)])]

groupies = [# Group(i) for i in ["  ", "  󱨠", "  ", "  ", "  "],
            Group(name="1", label="  "),
            Group(name="2", label=" 󱨠 "),
            Group(name="3", label="  "),
            Group(name="4", label="  "),
            Group(name="5", label="  "),
            Group(name="6", label=" 6 "),
            Group(name="7", label=" 7 "),
            ]

groups = scratchpads + groupies

for group in groupies:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            # Key(
            #    [_mod, "shift"],
            #    i.name,
            #    lazy.window.togroup(i.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            Key([mod, "shift"], group.name, lazy.window.togroup(group.name),
                desc="move focused window to group {}".format(group.name)),
        ]
    )


## --------------------  Layouts ----------------------------------------
# ----------------------------------------------------------------------
layouts = [
    layout.Columns(border_width=3, border_focus="#ffffff"),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(border_focus="#800080"),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.Floating(border_focus=colors.green, border_normal=colors.red, border_width=3)
]

floating_layout = layout.Floating(
    border_focus="#ffffff",
    border_normal="#0000ff",
    border_width=3,
    width=1000,
    height=500,
    float_rules=[
        Match(wm_type='utility'),
        Match(wm_type='notification'),
        Match(wm_type='toolbar'),
        Match(wm_type='splash'),
        Match(wm_type='dialog'),
        Match(wm_class='file_progress'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(func=lambda c: c.has_fixed_size()),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="pinentry-gtk-2"),  # GPG key password entry
    ]
)


## --------------------  Widgets ---------------------------------------
# ----------------------------------------------------------------------
# colors
white = "#ffffff"
black = "#000000"


# function for the powerline
def powerline(fg, bg):
    return widget.TextBox(
            foreground=fg,
            background=bg,
            fontsize=60,
            padding=-8,
            text="\ueb6f",)

# the window name parsing function
def parse_window_name(text):
    known_changed = {'mpv':'mpv', 'tebrow':'qutebrowser','Thunderb':'Thunderbird', 'Firef':'Firefox' }
    for abbre, app in known_changed.items():
        if abbre in text:
            return app + " | " + text[:50]
    known_left = ["Trans", "potif", "reOff"] 
    for app in known_left:
        if app in text:
            return text
    return "alacritty" + " | " +  text[:50]

# xdotool func for parsing the window class or name
def xdotool_parse_window_name(text):
    window_class = subprocess.run(["xdotool", "getwindowfocus", "getwindowclassname"], capture_output=True)
    return window_class.stdout.decode("utf-8")

def parse_windowname(text):
    """Return parsed window name for WindowName widget."""
    text_lst = text.split()
    if len(text_lst) > 2:
        #  text = text_lst[-1] + " : " + " ".join(text_lst[:-2])
        text = f"{text_lst[-1]} : {' '.join(text_lst[:-2])}"
    return text.replace("—", "-")

screens = [
    Screen(
        wallpaper='~/.config/qtile/assets/wallpapers/house_river_shore.jpg', 
        wallpaper_mode='stretch',
        top=bar.Bar(
            [
                widget.GroupBox(fontsize=22,
                                block_highlight_text_color='#000000',
                                borderwidth=3,
                                active="#ffffff",
                                this_current_screen_border="#F5F5F5",
                                foreground="#ffffff",
                                disable_drag=True,
                                inactive="#ffffff",
                                rounded=False,
                                highlight_color=["#000000", "#ffffff"],
                                fmt="{}",
                                highlight_method="block"),
                widget.CPU(fontsize=14,
                           format="  {freq_current}GHz {load_percent}%",
                           background=black,
                           foreground=white,
                           padding=5),
                widget.Spacer(length=20),
                widget.WindowName(
                    font="JetBrainsMono Nerd Font",
                    fmt="<b>{}</b>",
                    parse_text=parse_windowname,
                    fontsize=17,),
                widget.Spacer(length=40),
                widget.Chord(
                    foreground="#ff00ff",
                    ),
                widget.Spacer(length=20),
                powerline(fg=white, bg=black),
                widget.WindowCount(
                                 background=white,
                                 text_format="󰣇   {num} ",
                                 show_zero=True,
                                 foreground=black,),
                powerline(fg=black, bg=white),
                widget.Net(format='{down:.0f}{down_suffix}   {up:.0f}{up_suffix}',
                           ),
                powerline(fg=white, bg=black),
                widget.Wlan(format="   ",
                            interface="wlp0s20f3",
                            disconnected_message=" 󰤮 ",
                            background=white,
                            foreground=black,
                            ),
                powerline(fg=black, bg=white),
                widget.Backlight(backlight_name='intel_backlight',
                                 format='{percent:2.0%}',
                                 fmt='<b>󰃟   {}</b>',
                                 change_command="brightnessctl set {0}",
                                 background=black,
                                 foreground=white,
                                 ),
                powerline(fg=white, bg=black),
                widget.Battery(notify_below=30,
                               full_char="󱊣",
                               discharge_char="",
                               charge_char="󰂅",
                               empty_char="",
                               format="{char}   {percent:2.0%}",
                               background=white,
                               foreground=black,
                               ),
                powerline(fg=black, bg=white),
                widget.Volume(step=1,
                              fmt='<b>  {}</b>',
                              background=black,
                              foreground=white,
                              ),
                powerline(fg=white, bg=black),
                widget.Clock(format="󰅐   %I:%M  ",
                             background=white,
                             foreground=black,),
            ],
            size=24,
            background="#00000000",
        ),



    ),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=19,
    padding=4,
    fmt="<b>{}</b>",
)
extension_defaults = widget_defaults.copy()

## --------------------  Mouse ----------------------------------------
# ----------------------------------------------------------------------

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


'''
@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.client_new
def new_client(client):
    if client.name == "alacritty":
        client.togroup("1")
'''

main = None
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
