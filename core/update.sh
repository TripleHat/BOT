#!/bin/bash

echo "Updating..."

cd $HOME && rm -rf BOT

git clone https://github.com/TripleHat/BOT

cd BOT; bash install.sh

echo "Tool is updated"
sleep 2
clear
python3 bot.py
