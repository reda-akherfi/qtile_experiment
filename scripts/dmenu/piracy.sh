#!/bin/bash
#



torrent=$(echo "" | dmenu -p "Looking up torrents: "  -fn 'Roboto Mono-16' -l 10 -nb '#333333' -nf '#f5f5f5' -sf '#268bd2' -sb '#ffffff' )

torrent_keywords_pbays=$(echo $torrent | sed 's/ /&/g') 
torrent_keywords_1337=$(echo $torrent | sed 's/ /-/g') 
torrent_keywords_yts=$(echo $torrent | sed 's/ /%20/g') 
duck=$(echo $torrent | sed 's/ /+/g') 


pbays_url=$(echo ":open -t https://1337x.to/search/ababababa/1/;;open -t https://pirate-bays.net/search?q=rdrdrdrd;;open -t https://www.yst.mx/browse-movies/cdcdcdcd/all/all/0/latest/0/all;;tab-next" | sed -e "s/ababababa/$torrent_keywords_1337/g" -e "s/rdrdrdrd/$torrent_keywords_pbays/g" -e "s/cdcdcdcd/$torrent_keywords_yts/g")


qutebrowser --target window --set zoom.default 125  https://google.com/search?q=$duck "$pbays_url"
