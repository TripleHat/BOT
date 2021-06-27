#!/bin/bash

# Cheching Dependencies

for i in python play-audio python3; do
 if [[ -e $PATH/$i ]]; then
  echo "package $i Found!"
  sleep 1
 else
  echo "installing $i"
 sleep 1
  pkg install $i
 fi
done

for pyp in requests gTTS gtts ; do
 echo "installing $pyp"
 sleep 1
 pip3 install $pyp
done

clear; python bot.py
