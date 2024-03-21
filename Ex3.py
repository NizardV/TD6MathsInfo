from Ex1 import *
from Ex2 import *

def Base2To16(nb2) :
    return Base10To16(Base2To10(nb2))

def Base16To2(nb16) :
    return Base10To2(Base16To10(nb16))

nb2 = int(input('Entrez un nombre en base 2 :'))
print(Base2To16(nb2))

nb16 = input('Entrez un nombre en base 16 :')
print(Base16To2(nb16))
