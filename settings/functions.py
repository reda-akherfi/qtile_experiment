from libqtile import qtile


# function for Wlan widget ::: on click --> gets formatted network information
def get_network_info():
    qtile.cmd_spawn('kitty --hold sh -c "ip a"')


# for the Clock widget ::: to open calcurse
def open_calcurse():
    qtile.cmd_spawn('kitty --hold sh -c "calcurse"')


# get sensors when clicking on the Cpu widget
def get_sensors():
    qtile.cmd_spawn('kitty --hold sh -c "sensors"')
