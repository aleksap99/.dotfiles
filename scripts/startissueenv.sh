#!/bin/bash

serverDir="$HOME/Projects/issuetracker/server/"
clientDir="$HOME/Projects/issuetracker/client/"

# enable db service
sudo systemctl start mariadb.service
# Server
xdotool set_desktop 1
sleep 0.1
alacritty --title="server editor" --working-directory=$serverDir -e sh -c "bash -c 'nvim'; bash" &
sleep 0.5
xdotool key Super+m
alacritty --title="server" --working-directory=$serverDir -e sh -c "bash -c 'source ~/.sdkman/bin/sdkman-init.sh; sdk use java 11.0.2-open;sbt'" &
sleep 0.5
xdotool key --repeat 2 --delay 200 Super+l
xdotool key Super+m
sleep 0.3

# Client
xdotool set_desktop 2
sleep 0.1
alacritty --title="client editor" --working-directory=$clientDir -e sh -c "bash -c 'nvim'; bash" &
sleep 0.5
xdotool key Super+m
alacritty --title="client" --working-directory=$clientDir -e sh -c "bash -c 'npm start'; bash" &
sleep 0.5
xdotool key --repeat 2 --delay 200 Super+l
xdotool key Super+m

