from Crypto import Random
from Crypto.Cipher import AES
import base64

f = open("q7.txt")
s = f.read()
s = s.decode('base64')
aes_obj = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
plain_text = aes_obj.decrypt(s)
print plain_text