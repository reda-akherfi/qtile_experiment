#!/bin/bash
#
# selected=$(echo -e "Option 1\nOption 2\nOption 3" | dmenu -p "Choose an option:")

word=$(echo "" | dmenu -p "Enter a word"  -fn 'Roboto Mono-16' -l 10 -nb '#333333' -nf '#f5f5f5' -sf '#268bd2' -sb '#ffffff')

qutebrowser --set zoom.default 125  --target window https://www.merriam-webster.com/dictionary/$word
