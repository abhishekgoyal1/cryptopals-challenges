from Crypto.Cipher import AES
from os import urandom
from random import randint

def xor(x1, x2):
	if (len(x1)<len(x2)):
		for i in range(len(x2)-len(x1)):
			x1= x1+" "
	return ''.join(chr(ord(a)^ord(b)) for a, b in zip(x1, x2)) 

def pad(block_size,s):
	tmp = len(s)%block_size
	if (tmp == 0):
		tmp = block_size
	else:
		tmp = block_size - tmp
	for i in range(tmp):
		s=s + chr(block_size)
	return s

def decrypt_ecb(key,m):
	aes_ecb = AES.new(key, AES.MODE_ECB)
	pt = aes_ecb.decrypt(m)
	return pt

def encrypt_ecb(key,m):
	m= pad(16,m)
	aes_ecb = AES.new(key, AES.MODE_ECB)
	ct = aes_ecb.encrypt(m)
	return ct

def encrypt_cbc(iv,pt,key):
	blocklen= len(iv)
	cipher_text=""
	aes_ecb = AES.new(key, AES.MODE_ECB)
	for i in range(0,len(pt),blocklen):
		if (i+blocklen<len(pt)):
			substr = pt[i:i+blocklen]
		else:
			substr = pt[i:len(pt)]
		xor_m = xor(substr,iv)
		ct = aes_ecb.encrypt(xor_m)
		iv = (ct)		
		cipher_text = cipher_text + ct
	return cipher_text

def enc_oracle(m):
	key= urandom(16)
	iv= urandom(16)
	pre = randint(5, 10)
	suf = randint(5, 10)
	pt= urandom(pre)+m+urandom(suf)
	mode= randint(0,1)
	if (mode==1):
		ct= encrypt_cbc(iv,pt,key)
	else:
		ct= encrypt_ecb(key,pt)
	return (ct,mode)

def detect_mode(m):
	(ct,mode)= enc_oracle(m)
	if (mode==0):
		actual="ecb"
	else:
		actual="cbc"
	blockcount=0
	uniqcount=0
	blocklist=[]
	for i in range(0,len(ct),16):
		block=ct[i:i+16]
		blockcount=blockcount+1
		if (block not in blocklist):
			blocklist.append(block)
			uniqcount=uniqcount+1
	# print blockcount
	# print uniqcount
	if (blockcount==uniqcount):
		print ("Detected: cbc, Actual: "+ actual)
	else:
		print ("Detected: ECB, Actual: "+ actual)
	
m= ""
for i in range(130):
	m=m+"asd"

detect_mode(m)