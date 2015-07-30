#!/usr/bin/python

import sys
import jujuclient
from pprint import pprint

try:
    env_name = sys.argv[1]
except IndexError:
    env_name = 'local'

env = jujuclient.Environment.connect(env_name)
watcher = env.watch()
while True:
    pprint(watcher.next())
