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
Using `cat -` does not work, because `-` is recognized as the standard input.
Using full path to access the file named '-'.
```
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

## level 3
passwd: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

### solution
Using `\` to escape the space character.
```
bandit2@bandit:~$ cat spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

## level 4
passwd: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

### solution
Using `ls -a` to show the hidden files.
```
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

## level 5
passwd: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

### solution
Using `file` command to find the type of file content.
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
Using '-user' and '-group' options of `find` command.
Using '2>/dev/null' to filter out the errors due to permission.
```
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

## level 8
passwd: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

### solution
Using `grep`.
```
bandit7@bandit:~$ cat data.txt | grep 'millionth'
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

## level 9
passwd: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

### solution
Using `uniq` to filter out uniquely presented line.
Note that `uniq` only check adjecent lines, so the lines must be sorted by `sort` in advance.
```
bandit8@bandit:~$ cat data.txt | sort | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

## level 10
passwd: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

### solution
Using `strings` to filter out human-readable strings.
Using `-e` option of `grep` to filter out strings beginning with several `=` characters.
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
Using `base64 -d` to decode base64-encoded string.
```
bandit10@bandit:~$ cat data.txt | base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

## level 12
passwd: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

### solution
Using `tr` to translate the string.
Check `man tr` for how to specify the translation.
```
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

## level 13
passwd: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

### solution
First use `xxd -r` to reverse the hexdump to its original file.
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
Using `-i` option of `ssh` to provide private SSH key.
```
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
# logged in the server as the user bandit14
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

## level 15
passwd: BfMYroe26WYalil77FoDi9qh59eK5xNr

### solution
Using `telnet` to communicate with process listening on specific port.
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