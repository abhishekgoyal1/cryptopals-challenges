from base64 import b64decode
from Crypto.Cipher import AES
from os import urandom
from random import randint

def xor(x1, x2):
	if (len(x1)<len(x2)):
		for i in range(len(x2)-len(x1)):
			x1= x1+" "
	return ''.join(chr(ord(a)^ord(b)) for a, b in zip(x1, x2)) 


def encrypt_ecb(key,m):
	m= pad(len(key),m)
	ecb_obj = AES.new(key, AES.MODE_ECB)
	cipher_text = ecb_obj.encrypt(m)
	return cipher_text

def pad(block_size,s):
	tmp = len(s)%block_size
	if (tmp == 0):
		tmp = block_size
	else:
		tmp = block_size - tmp
	for i in range(tmp):
		s=s + chr(block_size)
	return s
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

def enc_oracle(pre,m,key):
	iv= urandom(16)
	post="Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"
	post= post.decode('base64')
	pt=pre+m+post
	mode= 0
	if (mode==1):
		ct= encrypt_cbc(iv,pt,key)
	else:
		ct= encrypt_ecb(key,pt)
	return ct

def detect_mode(ct,block_len):
	blockcount=0
	uniqcount=0
	blocklist=[]
	for i in range(0,len(ct),block_len):
		block=ct[i:i+block_len]
		blockcount=blockcount+1
		if (block not in blocklist):
			blocklist.append(block)
			uniqcount=uniqcount+1
	if (blockcount==uniqcount):
		print ("Detected: cbc")
	else:
		print ("Detected: ecb")
	return

def detect_block_size(pre,key):
	pt= ""
	for i in range(100):
		pt=pt+'A'
	ct= enc_oracle(pre,pt,key)
	block_len=0
	tot_max=0
	for i in range(5,100):
		curmax=0
		for j in range(0,len(ct),i):
			if j+i<len(ct):
				if (ct[j:j+i] in ct[j+i:j+2*i] and ct[j:j+i/2] not in ct[j+i/2:j+i] and ct[j:j+i/3] not in ct[j+i/3:j+2*i/3]):
					curmax=curmax+1
		if (curmax>tot_max):
			block_len=i
	return block_len

def detect_presize(pre,key,block_len):
	temp=""
	presize=0
	presize_mult=0
	for i in range(2*block_len-1):
		temp=temp+"A"
	for i in range(100):
		temp=temp+"A"
		ct= enc_oracle(pre,temp,key)
		for j in range(0,len(ct),block_len):
			if j+block_len<len(ct):
				if (ct[j:j+block_len] in ct[j+block_len:j+2*block_len]):
					presize=j-i
					break
		if (presize!=0):
			break
	return presize


key= urandom(16)
pre= urandom(randint(5,100))
print len(pre)
block_len= detect_block_size(pre,key)
print (block_len)
presize= detect_presize(pre,key,block_len)
print presize
init_len=0
for i in range(0,200,block_len):
	if i>=presize:
		init_len=i
		break
print init_len
init_str=""
for i in range(presize,init_len):
	init_str=init_str+"A"
temp=""
for i in range(block_len):
	temp=temp+"A"
unknown=""
temp2=""
start=init_len
index=0
for i in range(200):
	init=init_str
	if (index==block_len):
		index=0
		temp2=temp2+temp
		start=start+block_len
	for k in range(block_len-index-1):
		init=init+"A"
	ct1= enc_oracle(pre,init,key)
	for j in range(256):
		curr= init+unknown+chr(j)
		ct= enc_oracle(pre,curr,key)
		if (ct1[start:start+block_len] in ct[start:start+block_len]):
			unknown=unknown+chr(j)
			break
	index=index+1
print (unknown)
