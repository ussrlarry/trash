#!/usr/bin/env python

import os, sys
import requests
import json
from urlparse import urlparse

ci_id = [4712, 5614, 5407, 5197, 5609, 5531, 5620,
         5018, 5458, 5113, 4666, 4161, 4596, 4935,
         4936, 5622, 5623, 5624, 5625, 5626, 5627,
         5628, 5630, 5631, 5632]

compaigns_dict_chrome = {}
diff_list = []

f = open(".token","r")
token = f.readline().rstrip()

for i in ci_id:
    params = (
    ('ci', i),
    ('h', token),
    )

    response = requests.get('http://api.dynamicspots.bid/admin/', params=params)
    chrome_urls = urlparse(json.loads(response.content)["result"]["urls"]["CH"]).hostname
    compaigns_dict_chrome.update({i: chrome_urls})

#    with open('.compaigns_dict_chrome', 'w') as f:
#        json.dump(compaigns_dict_chrome, f, ensure_ascii=False)

with open('.compaigns_dict_chrome') as f:
    stored_compaigns_chrome = json.load(f)


for i in ci_id:
    if stored_compaigns_chrome.get('%s' % i) != compaigns_dict_chrome.get(i):
        diff_list.append("[%s:%s]" % (i, compaigns_dict_chrome.get(i)))

if len(diff_list) == 0:
    print "urls for chrome compaigns are valid"
    sys.exit(0)
elif len(diff_list) > 0:
    a = "".join(str(x) for x in diff_list)
    print ("urls changed: %s" % a)
    with open('.compaigns_dict_chrome', 'w') as f:
        json.dump(compaigns_dict_chrome, f, ensure_ascii=False)
    sys.exit(2)
else:
    print "ERR"
    sys.exit(1)
