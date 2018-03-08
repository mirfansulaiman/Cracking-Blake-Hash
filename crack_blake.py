#!/usr/bin/python3
# Name : Crack Blake Encryption
# Author: mirfansulaiman
# Indonesian Backtrack Team | Kurawa In Disorder |
# http://indonesianbacktrack.or.id
# http://mirfansulaiman.com/
# http://ctfs.me/
#
# this for BLAKE-512
# usage : python crack_blake.py
#
# tested on Linux kali 4.14.0-kali3-amd64 #1 SMP Debian 4.14.12-2kali1 (2018-01-08) x86_64 GNU/Linux 
# tested on Python 3.6.4
#
# have a bug? report to doctorgombal@gmail.com or PM at http://indonesianbacktrack.or.id/forum/user-10440.html
# Note : Dont change author name ! Fuck Plagiarism !

import hashlib

def bruteforce():
    with open("rockyou.txt" , encoding='utf-8', errors='ignore') as infile:
        answer= infile.read().splitlines()
        for check in answer:
            blake = hashlib.new('BLAKE2b512')
            blake.update(check.encode())
            print("Checking : {0}".format(check))
            if not blake.hexdigest() == '999999999999999999999999':
               print("You are noob ! :p \n")
            else:
               print("CRACKED ! : {0}".format(check))
               print("You are handsome guy !")
               break
               return

def encrypt(arg):
    blake = hashlib.new('BLAKE2b512')
    blake.update(arg.encode())
    chippertext = blake.hexdigest()
    return chippertext.upper()

if __name__ == '__main__':
        try:
            bruteforce()
            #print(encrypt('The quick brown fox jumps over the lazy dog'))
        except KeyboardInterrupt:
            print('bye bye..')
            exit(0)
