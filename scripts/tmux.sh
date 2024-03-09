if [ -z "$(pgrep tmux)" ]; then
    alacritty --command tmux  
else
    alacritty --command tmux attach
fi
