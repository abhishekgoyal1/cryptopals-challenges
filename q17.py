from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from os import urandom
from random import randint




def xor(x1, x2):
	if (len(x1)<len(x2)):
		for i in range(len(x2)-len(x1)):
			x1= x1+" "
	return ''.join(chr(ord(a)^ord(b)) for a, b in zip(x1, x2)) 


def decrypt_ecb(key,m):
	ecb_obj = AES.new(key, AES.MODE_ECB)
	plain_text = ecb_obj.decrypt(m)
	return plain_text

def encrypt_ecb(key,m):
	m= pad(len(key),m)
	ecb_obj = AES.new(key, AES.MODE_ECB)
	cipher_text = ecb_obj.encrypt(m)
	return cipher_text


def decrypt_cbc(iv,ct, key):
	blocklen = len(iv)
	plain_text = ""
	for i in range(0,len(ct),blocklen):
		substr = (ct[i:i+blocklen])
		temp = decrypt_ecb(key,substr)
		xor_m = xor(temp,iv)
		iv = (substr)		
		plain_text = plain_text + xor_m

	return plain_text

def encrypt_cbc(iv,pt,key):
	blocklen= len(iv)
	cipher_text=""
	cbc_obj = AES.new(key, AES.MODE_ECB)
	for i in range(0,len(pt),blocklen):
		if (i+blocklen<len(pt)):
			substr = (pt[i:i+blocklen])
		else:
			substr = (pt[i:len(pt)])
		xor_m = xor(substr,iv)
		ct = cbc_obj.encrypt(xor_m)
		iv = (ct)		
		cipher_text = cipher_text + ct
	return cipher_text

def pad(s,block_len):

	tmp = len(s)
	padding_len = (block_len-tmp%block_len)
	for i in range(padding_len):
		s = s + chr(padding_len)
	return s

def fun1(strings, key):
	choice= randint(0,9)
	pt= strings[choice].decode('base64')
	iv = urandom(16)
	pt= pad(pt,16)
	print pt
	ct= encrypt_cbc(iv,pt,key)
	return (ct,iv)

def padding_check(pt):
	pad = pt[-1]
	for i in range(ord(pad)):
		if (pt[-i - 1] != pad):
			return False
	return True

def fun2(ct,iv,key):
	pt= decrypt_cbc(iv,ct,key)
	return padding_check(pt)




strings="MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=\nMDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=\nMDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==\nMDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==\nMDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl\nMDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==\nMDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==\nMDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=\nMDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=\nMDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"

strings=strings.split('\n')
key= urandom(16)
[ct,iv]= (fun1(strings,key))
print (ct)
print fun2(ct,iv,key)
