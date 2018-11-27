from base64 import b64decode
from Crypto.Cipher import AES



def xor(data, key):
	if (len(data)<len(key)):
		for i in range(len(key)-len(data)):
			data= data+chr(0)
	return ''.join(chr(ord(a)^ord(b)) for a, b in zip(data, key)) 

def ctr_encrypt(pt,key,iv,block_len):
	counter=0
	rem= len(pt)%block_len
	blockcount=len(pt)/block_len
	if (rem>0):
		blockcount=blockcount+1
	ctr=""
	ct=""
	aes_obj = AES.new(key, AES.MODE_ECB)
	start=0
	end= block_len
	for i in range(blockcount):
		inp2= chr(counter)+ctr
		for j in range(block_len/2-len(inp2)):
			inp2=inp2+chr(0)
		inp= iv+inp2
		op= aes_obj.encrypt(inp)
		if (end>=len(pt)):
			end=len(pt)
		ct1= xor(pt[start:end],op)
		ct= ct+ct1
		counter=counter+1
		if (counter==256):
			counter=0
			val= ord(ctr)
			ctr= chr(val+1)
		start=start+block_len
		end= start+block_len

	return ct

pt= "L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=="
pt= pt.decode('base64')
key="YELLOW SUBMARINE"
iv=""
for i in range(8):
	iv=iv+chr(0)
print ctr_encrypt(pt,key,iv,16)