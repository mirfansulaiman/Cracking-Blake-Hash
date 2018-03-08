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
# have a bug? report to doctorgombal@gmail.com or PM at http://indonesianbacktrack.or.id/forum/user-10440.html
# Note : Dont change author name ! Fuck Plagiarism !

import hashlib

def bruteforce():
    with open("rockyou.txt", encoding='utf-8', errors='ignore') as infile:
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

if __name__ == '__main__':
        try:
            bruteforce()
        except KeyboardInterrupt:
            print('bye bye..')
            exit(0)
