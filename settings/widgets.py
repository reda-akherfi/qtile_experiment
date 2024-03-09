from libqtile import bar, widget
from libqtile.config import Screen

import subprocess

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
                widget.Spacer(length=20),
                widget.WindowName(
                    font="JetBrainsMono Nerd Font",
                    fmt="<b>{}</b>",
                    parse_text=parse_window_name,
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
