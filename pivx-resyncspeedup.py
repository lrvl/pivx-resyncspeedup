#!/usr/bin/env python3
import os
import subprocess
import json
import pprint

# Screenshot of improved bandwidth -> http://imgur.com/a/H2Cpt
# External tools (overwrite from env if needed)
PIVXCLI = os.getenv('PIVXCLI','./pivx-cli')

json_data = subprocess.check_output([PIVXCLI, "getpeerinfo"]).decode("utf-8").splitlines()
json_data_str = ''.join(str(e) for e in json_data)
peerinfo = json.loads(json_data_str)

for peer in peerinfo:
    if peer['pingtime'] > 0.2:
        print("%s" % peer['addr'].split(":")[0])
