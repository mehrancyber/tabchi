#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import os
redis = redis.Redis('localhost')
id = input("Enter SinChi Number (1,2,3,4,5,...) : ")
source = os.popen("cat ./bot.lua").read()
launcher = """#!/bin/bash 
COUNTER=0
while [  $COUNTER -lt 5 ]; do
kill $(pgrep telegram-cli)
  ./tg -p sinxt-{} -s bot.lua
sleep 0.1
done""".format(id,id)
newlauncher = open("sinxt-{}.sh".format(id),"w")
newlauncher.write(launcher)
newlauncher.close()
os.popen("chmod 777 sinxt-{}.sh".format(id))
print("Done!\nNew SinChi Created...\n SinChi ID : {}\nRun : ./sinxt-{}.sh".format(id,id))
