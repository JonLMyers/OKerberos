from Crypto.Cipher import ARC4
from Crypto.Hash import HMAC, MD5, MD4
from getpass import getpass
from struct import pack


def encrypt(etype, key, msg_type, data):
    pass


def decrypt(etype, key, msg_type, encrypted):
    pass

if __name__ == '__main__':
     user = input("Username:")
     getpass('Password:')
