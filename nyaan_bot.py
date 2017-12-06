#!/usr/bin/env python
# coding: utf-8

import os
import nyaan_bot_env
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(18, GPIO.FALLING, bouncetime=200)
GPIO.add_event_detect(19, GPIO.FALLING, bouncetime=200)
str = ''
count = 0
count2= 0
nya = 5
pin18=False
pin19=False
count = -4
while True:
  if count <= -100:
    count = -100
  if GPIO.input(19):
    count2 += 1
    if count2 >= 50:
      os.system("sudo shutdown -h now")
      break
  else:
    count2=0
  if count == -3:
     str += 'ん'
  if GPIO.input(18):
    if count  <= 0:
      str += 'にゃ'
      count = 0
    count += 1
    if 5 <= count:
      str += 'ー'
  else:
    if 0 < count:
      count = 0
    else:
      count -= 1
  if count <= -60 and not str == '':
    str += '\n by raspberry pi'
    nyaan_bot_env.api.update_status(status=str)
    str = ''
    count = -4
  time.sleep(0.05)
GPIO.cleanup(18)
GPIO.cleanup(19)
