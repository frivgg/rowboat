from time import sleep
from utils import SETTINGS
from namelib import generateName
import requests
import os

print(
    """                      __                __   
 .----.-----.--.--.--|  |--.-----.---.-|  |_ 
 |   _|  _  |  |  |  |  _  |  _  |  _  |   _|
 |__| |_____|________|_____|_____|___._|____|
    rowboat for roblox, ipban guaranteed\n"""
)
i = 1
while os.path.exists("./logs/log%s.txt" % i):
    i += 1
input("log%s.txt" % i + " will be created. Press enter to continue.")
fh = open("./logs/log%s.txt" % i, "a")
for v in range(SETTINGS.iterations):
    usr = generateName(SETTINGS.algorithm, SETTINGS.length, SETTINGS.charSet)
    r = requests.get(SETTINGS.endpoint + usr)
    if "success" in r.json():
        fh.write(str(v) + " : " + usr + " : available" + "\n")
        fh.flush()
        os.fsync(fh.fileno())
        print(str(v) + " : " + usr + " : available")
    else:
        print(str(v) + " : " + usr + " : taken")

    sleep(SETTINGS.delay / 1000)
