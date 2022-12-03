#!/bin/bash




currentlayout=`xkb-switch`

if [ $currentlayout = "us" ]
then
  setxkbmap rs latin 
elif [ $currentlayout = "rs(latin)" ]
then
  setxkbmap rs
else
  setxkbmap us
fi

exit
