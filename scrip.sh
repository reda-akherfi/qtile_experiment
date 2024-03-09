Xephyr -br -ac -noreset -screen 1920x1080 :1 &
sleep 3
DISPLAY=:1 qtile start -c /home/reda/redalo_setup/qtile_shit/qtile01v/config.py &

