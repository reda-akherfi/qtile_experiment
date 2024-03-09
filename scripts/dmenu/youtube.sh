#!/bin/bash
#
#
#


# down the road i need to make it search for multiple things

youtube_search=$(echo "" | dmenu -p "Searching Youtube for :" -fn 'Roboto Mono-16' -l 10 -nb '#333333' -nf '#f5f5f5' -sf '#268bd2' -sb '#ffffff')

yt=$(echo $youtube_search | sed -e "s/ /+/g")

qutebrowser --set zoom.default 125  --target window https://www.youtube.com/results?search_query=$yt

