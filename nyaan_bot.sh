#!/bin/sh

mkdir -p /usr/share/twitter_bot
cp -u ./nyaan_bot.py /usr/share/twitter_bot
cp -u ./nyaan_bot_env.py /usr/share/twitter_bot
cp -u ./nyaan_bot.service /etc/systemd/system/
