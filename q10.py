from Crypto.Cipher import AES

def xor(x1, x2):
	if (len(x1)<len(x2)):
		for i in range(len(x2)-len(x1)):
			x1= x1+" "
	return ''.join(chr(ord(a)^ord(b)) for a, b in zip(x1, x2)) 


def decrypt_ecb(key,m):
	aes_ecb = AES.new(key, AES.MODE_ECB)
	pt = aes_ecb.decrypt(m)
	return pt

def encrypt_ecb(key,m):
	aes_ecb = AES.new(key, AES.MODE_ECB)
	ct = aes_ecb.encrypt(m)
	return ct


def decrypt_cbc(iv,ct, key):
	blocklen = len(iv)
	plain_text = ""
	for i in range(0,len(ct),blocklen):
		substr = ct[i:i+blocklen]
		temp = decrypt_ecb(key,substr)
		xor_m = xor(temp,iv)
		iv = substr		
		plain_text = plain_text + xor_m

	return plain_text

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

key = "YELLOW SUBMARINE"
iv = "0000000000000000"
print ("=====================")
m= "HI I AM ASDFGHJKL"
ct= encrypt_cbc(iv,m,key)
print ("ENCRYPTION IS: ")
print ct
print ("DECRYPTED:")
print decrypt_cbc(iv,ct,key)