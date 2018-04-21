from Crypto.Cipher import ARC4
from Crypto.Hash import HMAC, MD5, MD4
from getpass import getpass
from struct import pack
import base

from okerberos.utils import encode


def encrypt(etype, key, msg_type, data):
    pass


def decrypt(etype, key, msg_type, encrypted):
    pass

if __name__ == '__main__':
     user = input("Username:")
     passwd = getpass('Password:')
     Credentials(user,passwd)


class Credentials(object):

    username = None
    password = None

    def __init__(self):
        self.username = username
        self.password = password

    def toDict(self,encoding = None):
        if encoding is None:
            return {"username" : self.username, "password" : self.password}
        else:
            return {"username" : encode(self.username), "password" : encode(self.password) }
