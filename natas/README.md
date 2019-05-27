# Natas

user: natas{level} \
website: `http://natas{level}.natas.labs.overthewire.org` \
__All passwords are also stored in /etc/natas_webpass/.__

## level 0
passwd: natas0

## level 1
passwd: gtVrDuiDfck831PqWsLEZy5gyDz1clto

### solution
Use Chrome to check the page source code. \
![Level 1](level_1.png)

## level 2
passwd: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

### solution
Same as level 1. \
![Level 2](level_2.png)

## level 3
passwd: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14

### solution
Check page source, we find that there is a folder `files`. \
![Level 3 - 1](level_3-1.png)

Try to access the folder directly. Something interesting shows up. Click and open `users.txt`. \
![Level 3 - 2](level_3-2.png)

The `users.txt` contains the password for natas3. \
![Level 3 - 3](level_3-3.png)

## level 4
passwd: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

### solution
Check the page source. There is a comment saying that "Not even Google will find it this time". Maybe it has something to do with web crawler. \
![Level 4 - 1](level_4-1.png)

Check `robots.txt`. \
![Level 4 - 2](level_4-2.png)

Check `/s3cr3t`. Bingo! \
![Level 4 - 3](level_4-3.png)

The password of natas4: \
![Level 4 - 4](level_4-4.png)
