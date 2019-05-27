# Bandit

server: bandit.labs.overthewire.org \
port: 2220 \
user: bandit{level} \
ssh login: ssh -p 2220 bandit{level}@bandit.labs.overthewire.org

## level 0
passwd: bandit0

## level 1
passwd: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

### solution
```
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

## level 2
passwd: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

### solution  
Use full path to access the file named '-'. \
_Note_: `cat -` does not work, because `-` is recognized as the standard input.
```
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

## level 3
passwd: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

### solution
Use `\` to escape the space character.
```
bandit2@bandit:~$ cat spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

## level 4
passwd: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

### solution
Use `ls -a` to show the hidden files.
```
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

## level 5
passwd: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

### solution
Use `file` command to find the type of the file content.
```
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

## level 6
passwd: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

### solution
Use `find` with `-size` and `! -executable` options.
```
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere02  maybehere04  maybehere06  maybehere08  maybehere10  maybehere12  maybehere14  maybehere16  maybehere18
maybehere01  maybehere03  maybehere05  maybehere07  maybehere09  maybehere11  maybehere13  maybehere15  maybehere17  maybehere19
bandit5@bandit:~/inhere$ find . -size 1033c ! -executable
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

## level 7
passwd: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

### solution
Use `-user` and `-group` options of `find` command. \
Use '2>/dev/null' to filter out the errors due to permission.
```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

## level 8
passwd: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

### solution
Use unix pipe and `grep`.
```
bandit7@bandit:~$ cat data.txt | grep 'millionth'
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

## level 9
passwd: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

### solution
Use `uniq` to filter out uniquely presented line. \
_Note_: `uniq` only check adjecent lines, so the lines must be sorted by `sort` in advance.
```
bandit8@bandit:~$ cat data.txt | sort | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

## level 10
passwd: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

### solution
Use `strings` to filter out human-readable strings. \
Use `-e` option of `grep` to filter out strings beginning with several `=` characters.
```
bandit9@bandit:~$ strings data.txt | grep -e '^==*'
========== password
========== isa
=FQ?P\U
=	F[
=)$=
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

## level 11
passwd: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

### solution
Use `base64 -d` to decode base64-encoded string.
```
bandit10@bandit:~$ cat data.txt | base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

## level 12
passwd: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

### solution
Use `tr` to translate the string. \
Check `man tr` for how to specify the translation.
```
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

## level 13
passwd: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

### solution
First use `xxd -r` to reverse the hexdump to its original file. \
Then repeat the following procedure until we get a ASCII text file:
1. use `file` to get the content type of the (last obtained) file
2. if the content type is `ASCII text`, then `cat`to get the password. END
3. if the content type is `gzip compressed data`, then `gunzip {filename}.gz`. GOTO 1 \
  Note that the file must be renamed to `*.gz`.
4. if the content type is `bzip2 compressed data`, then `bunzip2 {filename}.bz2`. GOTO 1 \
  The `bunzip2` command does not require a file with name in `*.bz2` format, but the output filename will be different for different types of input filenames. For `{filename}.bz2`, the output filename is `{filename}`. Check `man bzip2` for other cases.
5. if the content type is `POSIX tar archive (GNU)`, then `tar -xf {filename}`. GOTO 1

## level 14
passwd: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

### solution
Use the `-i` option of `ssh` to provide private SSH key.
```
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
# logged in the server as the user bandit14
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

## level 15
passwd: BfMYroe26WYalil77FoDi9qh59eK5xNr

### solution
Use `telnet` to communicate with process listening on a specific port.
```
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr

Connection closed by foreign host.
```

## level 16
passwd: cluFn7wTiGryunymYOu4RcffSxQluehd

### solution
Use `openssl s_client` to communicate with processes using SSL encryption.
```
bandit15@bandit:~$ openssl s_client -connect localhost:30001 -quiet
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd
```

## level 17
passwd: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn

### solution
1. Use `nmap` with `-p` option to scan open ports in a given range.
2. use `openssl s_client` to test if the processes speak SSL.
```
bandit16@bandit:~$ nmap -p31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2019-05-25 19:52 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00020s latency).
Not shown: 998 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
bandit16@bandit:~$ openssl s_client -connect localhost:31046 -quiet
140708919428352:error:141A10F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:269:
bandit16@bandit:~$ openssl s_client -connect localhost:31691 -quiet
139808354964736:error:141A10F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:269:
bandit16@bandit:~$ openssl s_client -connect localhost:31790 -quiet
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```

3. Copy the private key into a file `ssh_key` and use `ssh` with `-i` option to log in as bandit17.

4. Get the password of bandit17.
```
bandit17@bandit:~$ cat /etc/bandit_pass/bandit17
xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
```

## level 18
passwd: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

### solution
Use `diff` to check the differences between two text files.
```
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< hlbSBPAWJmL6WFDb06gpTx1pPButblOA
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

## level 19
passwd: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

### solution
From `man ssh`:
```
ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface] [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
         [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11] [-i identity_file] [-J destination] [-L address]
         [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port] [-Q query_option] [-R address] [-S ctl_path]
         [-W host:port] [-w local_tun[:remote_tun]] destination [command]
```
We can pass the command `cat ~/readme` to get the password:
```
❡ ssh -p 2220 bandit18@bandit.labs.overthewire.org "cat ~/readme"
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

## level 20
passwd: GbKksEFF4yrVs6il55v6gwY5aVje5f0j

### solution
Google `setuid` to understand how the `./bandit20-do` works.
```
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

## level 21
passwd: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

### solution
Use `nc` with option `-l` to start a tcp network daemon. \
Use `tmux` for effective client-server messaging.
![Level 21](level21.png)

## level 22
passwd: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

### solution
Check the `cron` task for bandit22.
```
bandit21@bandit:/etc/cron.d$ cd
bandit21@bandit:~$ cd /etc/cron.d
bandit21@bandit:/etc/cron.d$ ls
cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

## level 23
passwd: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

### solution
Check the `cron` task for bandit23. \
The script `/usr/bin/cronjob_bandit23.sh` creates an encrypted filename using the username (`$(whoami)`) and copies the password into a file with that name under the folder`/tmp`. The corresponding filename for bandit23 can be obtained by replacing `$myname` in `mytarget` with `bandit23`.
```
bandit22@bandit:~$ cd /etc/cron.d
bandit22@bandit:/etc/cron.d$ ls
cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:/etc/cron.d$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

## level 24
passwd: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

### solution
Check the `cron` task for bandit24. \
The script `/usr/bin/cronjob_bandit24.sh` executes and deletes all scripts in `/var/spool/bandit24` every minute. \
To obtain the password for bandit24, we can write a bash script to copy the password into a file under `/tmp` folder.
```
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/hhh123456
```
Don't forget to use `chmod +x` to give the script permission for execution.

The terminal log:
```
bandit23@bandit:/etc/cron.d$ cat cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
	echo "Handling $i"
	timeout -s 9 60 ./$i
	rm -f ./$i
    fi
done



bandit23@bandit:/etc/cron.d$ vim /var/spool/bandit24/haha
bandit23@bandit:/etc/cron.d$ chmod +x /var/spool/bandit24/haha
bandit23@bandit:/etc/cron.d$ cat /var/spool/bandit24/haha
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/hhh123456
bandit23@bandit:/etc/cron.d$ cat /tmp/hhh123456
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

## level 25
passwd: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

### solution
The solution __should be__:
```
for pin in {0000..9999}; do echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ ${pin}"; done | nc localhost 30002 | grep -v "Wrong"
```
However, the daemon on port 30002 was not working... I found one daemon on port 30003 that seems to be an alternative (someone might find out the port 30002 was not working and rescued the level by uploading his/her implementation). After tons of attempts I found that the pin code is `5591`. A strange thing is, the following command will get different result randomly:
```
bandit24@bandit:~$ for pin in {5588..5706}; do echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ ${pin}"; done | nc localhost 30003
```
![Level 25 Bug](level25_bug.png)

## level 26 and 27
level 26 passwd: 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z \
level 27 passwd: 3ba3118a22e93127a4ed485be72ef5ea

### solution
It is the most interesting challenge so far. \
First check the login shell of bandit26:
```
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```
From the bash script we can tell that when bandit26 is logged in, a `more` command will be executed, then the shell will exit. We can try to login in as bandit26:
```
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost
Could not create directory '/home/bandit25/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit25/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

...
...
...

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us through IRC on
  irc.overthewire.org #wargames.

  Enjoy your stay!

  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
Connection to localhost closed.
bandit25@bandit:~$
```
The content of `/home/bandit26/text.txt` is
```
  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
```
The login shell exited because the `more` command had displayed the whole content of `/home/bandit26/text.txt`. To make the login shell stop at the `more` command, we can __resize the terminal window__. The key idea is that when the content does not fit the terminal window, the `more` command will display the content in pages.

![Level 26 - Resize window](level26_resize_window.png)

When in `more` mode, we can type `v` to enter `vim` editor mode. Note that the shell used by the vim editor is still the login shell. So shell command such as `:!ls` will not work as expected. We can use `:set shell=/bin/bash` to fix that.

Now we should have a shell working and we can get the passwords of level 26 and level 27.
```
:!cat /etc/bandit_pass/bandit26
5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

:!./bandit27-do cat /etc/bandit_pass/bandit27
3ba3118a22e93127a4ed485be72ef5ea
```

## level 28
passwd: 0ef186ac70e04ea33b4c1853d2526fa2

### solution
Use `git clone`. \
Note that we can not clone the repo in home directory. We can create a temporary direcotry by `mktemp -d`.
```
bandit27@bandit:~$ mktemp -d
/tmp/tmp.fLNqrZBgEo
bandit27@bandit:~$ cd /tmp/tmp.fLNqrZBgEo
bandit27@bandit:/tmp/tmp.fLNqrZBgEo$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit27/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password:
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/tmp.fLNqrZBgEo$ ls
repo
bandit27@bandit:/tmp/tmp.fLNqrZBgEo$ cd repo/
bandit27@bandit:/tmp/tmp.fLNqrZBgEo/repo$ ls
README
bandit27@bandit:/tmp/tmp.fLNqrZBgEo/repo$ cat README
The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2
```

## level 29
passwd: bbc96594b4e001778eee9975372716b2

### solution
Use `git log` to check commit history. \
Use `git show` to check the diff of a specific commit.
```
bandit28@bandit:~$ mktemp -d
/tmp/tmp.BlZyRojABl
bandit28@bandit:~$ cd /tmp/tmp.BlZyRojABl
bandit28@bandit:/tmp/tmp.BlZyRojABl$ ls
bandit28@bandit:/tmp/tmp.BlZyRojABl$ git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit28/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit28-git@localhost's password:
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0)
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/tmp.BlZyRojABl$ ls
repo
bandit28@bandit:/tmp/tmp.BlZyRojABl$ cd repo/
bandit28@bandit:/tmp/tmp.BlZyRojABl/repo$ ls
README.md
bandit28@bandit:/tmp/tmp.BlZyRojABl/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
bandit28@bandit:/tmp/tmp.BlZyRojABl/repo$ git log
commit 073c27c130e6ee407e12faad1dd3848a110c4f95
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    fix info leak

commit 186a1038cc54d1358d42d468cdc8e3cc28a93fcb
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    add missing data

commit b67405defc6ef44210c53345fc953e6a21338cc7
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    initial commit of README.md
bandit28@bandit:/tmp/tmp.BlZyRojABl/repo$ git show 186a
commit 186a1038cc54d1358d42d468cdc8e3cc28a93fcb
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    add missing data

diff --git a/README.md b/README.md
index 7ba2d2f..3f7cee8 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials

 - username: bandit29
-- password: <TBD>
+- password: bbc96594b4e001778eee9975372716b2

bandit28@bandit:/tmp/tmp.BlZyRojABl/repo$
```

## level 30
passwd: 5b90576bedb2cc04c86a9e924ce42faf

### solution
Use `git branch` and `git checkout` to check and switch to other branches.
```
bandit29@bandit:~$ mktemp -d
/tmp/tmp.xZhUNEYJdH
bandit29@bandit:~$ cd /tmp/tmp.xZhUNEYJdH
bandit29@bandit:/tmp/tmp.xZhUNEYJdH$ git clone ssh://bandit29-git@localhost/home/bandit29-git/repo
Cloning into 'repo'...

...
...
...

Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (2/2), done.
bandit29@bandit:/tmp/tmp.xZhUNEYJdH$ ls
repo
bandit29@bandit:/tmp/tmp.xZhUNEYJdH$ cd repo/
bandit29@bandit:/tmp/tmp.xZhUNEYJdH/repo$ ls
README.md
bandit29@bandit:/tmp/tmp.xZhUNEYJdH/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

bandit29@bandit:/tmp/tmp.xZhUNEYJdH/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
bandit29@bandit:/tmp/tmp.xZhUNEYJdH/repo$ git checkout dev
Branch dev set up to track remote branch dev from origin.
Switched to a new branch 'dev'
bandit29@bandit:/tmp/tmp.xZhUNEYJdH/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: 5b90576bedb2cc04c86a9e924ce42faf

bandit29@bandit:/tmp/tmp.xZhUNEYJdH/repo$
```

## level 31
passwd: 47e603bb428404d265f59c42920d81e5

### knowledge
git object: commit, tree (folder), blob (file) \
refs: named references to git objects, the value of a ref is the SHA-1 value of the referenced git object \
tag: a kind of ref \
`git pack-refs`: Pack refs in `.git/refs` into a file `.git/packed-refs`. The tags in `.git/refs/tags` will be removed after packing. \
`git gc`: Pack all objects in `.git/objects` into `.git/objects/pack`.

### solution
Use `git tag` to check tags. \
Use `git show` to check the content of the object to which the tag refers.
```
bandit30@bandit:~$ mktemp -d
/tmp/tmp.McQB94K2fP
bandit30@bandit:~$ cd /tmp/tmp.McQB94K2fP
bandit30@bandit:/tmp/tmp.McQB94K2fP$ git clone ssh://bandit30-git@localhost/home/bandit30-git/repo
Cloning into 'repo'...

...
...
...

remote: Counting objects: 4, done.
remote: Total 4 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (4/4), done.
bandit30@bandit:/tmp/tmp.McQB94K2fP$ ls
repo
bandit30@bandit:/tmp/tmp.McQB94K2fP$ cd repo/
bandit30@bandit:/tmp/tmp.McQB94K2fP/repo$ ls
README.md
bandit30@bandit:/tmp/tmp.McQB94K2fP/repo$ git tag
secret
bandit30@bandit:/tmp/tmp.McQB94K2fP/repo$ git show secret
47e603bb428404d265f59c42920d81e5
bandit30@bandit:/tmp/tmp.McQB94K2fP/repo$
```

### Reproducing
To show how the lab was created, we need to understand git objects and git refs. The steps for reproducing the lab:
```
mkdir repo
cd repo
git init
echo "just an epmty file... muahaha" > README.md
echo "47e603bb428404d265f59c42920d81e5" > secret_file
git add . # after git add, the two files are saved to .git/objects
find .git/objects/ -type f # get the SHA-1 value of the two objects
git show <SHA-1> # check which SHA-1 value is the secret_file
git tag secret <SHA-1_secret_file>
git reset secret_file # unstaging the secret_file does not affect .git/objects
rm secret_file # removing the secret_file does not affect .git/objects
git commit
git pack-refs # pack the tags into .git/packed-refs and remove .git/refs/tags/secret
```
The latecomers can use `git tag` to find the `secret` tag and use `git show` to get the content of `secret_file`.

### Take-home message
`git add` will permanently add files/folders to `.git/objects`.

## level 32
passwd: 56a9bf19c63d650ce78e6ec0354ee45e

### solution
```
bandit31@bandit:/tmp/tmp.h5oQZAACwy$ cd repo/
bandit31@bandit:/tmp/tmp.h5oQZAACwy/repo$ ls
README.md
bandit31@bandit:/tmp/tmp.h5oQZAACwy/repo$ cat README.md
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.h5oQZAACwy/repo$ echo 'May I come in?' > key.txt
bandit31@bandit:/tmp/tmp.h5oQZAACwy/repo$ git add key.txt
The following paths are ignored by one of your .gitignore files:
key.txt
Use -f if you really want to add them.
bandit31@bandit:/tmp/tmp.h5oQZAACwy/repo$ vim .gitignore # remove the line 'key.txt'
bandit31@bandit:/tmp/tmp.h5oQZAACwy/repo$ git add key.txt
bandit31@bandit:/tmp/tmp.h5oQZAACwy/repo$ git commit -m "Add key.txt"
[master b8c8ade] Add key.txt
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt
bandit31@bandit:/tmp/tmp.h5oQZAACwy/repo$ git push
Could not create directory '/home/bandit31/.ssh'.

...
...
...

Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 323 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: ### Attempting to validate files... ####
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
remote: Well done! Here is the password for the next level:
remote: 56a9bf19c63d650ce78e6ec0354ee45e
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
To ssh://localhost/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://bandit31-git@localhost/home/bandit31-git/repo'
bandit31@bandit:/tmp/tmp.h5oQZAACwy/repo$
```