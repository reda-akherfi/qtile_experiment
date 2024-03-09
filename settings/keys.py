from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord

mod = "mod4"
terminal = "alacritty"

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
