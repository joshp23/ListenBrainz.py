#!/usr/bin/env python3
# v 0.0.1
import sys
import os
from datetime import datetime, time
from urllib import request
import json
import config as cfg
import argparse
import pyperclip

parser = argparse.ArgumentParser(description='A bot for checking ListenBrainz stats')
parser.add_argument('-n','--notify', help='Display libnotify messages', action='store_true')
args = parser.parse_args()

if (args.notify):
    import subprocess as s

am = datetime.combine(datetime.today(), time.min)
am_ts = str(int(am.timestamp()))
pm = datetime.combine(datetime.today(), time.max)
pm_ts = str(int(pm.timestamp()))

url = 'http://api.listenbrainz.org/1/user/' + cfg.user + '/listens?max_ts=' + pm_ts + '&min_ts=' + am_ts
headers = {
 "User-Agent": "ListenBrainz.py/0.0.1 ( https://github.com/joshp23/ListenBrainz.py )", "Authorization": "Token {0}".format(cfg.api_key)
}
req = request.Request(url, headers=headers)
resp = request.urlopen(req)
data = json.load(resp)
var = str(data['payload']['count'])

pyperclip.copy(var)
print (var)

if (args.notify):
	s.call(['notify-send','Daily Scrobbles:', var ])
