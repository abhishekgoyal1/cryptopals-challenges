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

strings="SSBoYXZlIG1ldCB0aGVtIGF0IGNsb3NlIG9mIGRheQ==,Q29taW5nIHdpdGggdml2aWQgZmFjZXM=,RnJvbSBjb3VudGVyIG9yIGRlc2sgYW1vbmcgZ3JleQ==,RWlnaHRlZW50aC1jZW50dXJ5IGhvdXNlcy4=,SSBoYXZlIHBhc3NlZCB3aXRoIGEgbm9kIG9mIHRoZSBoZWFk,T3IgcG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==,T3IgaGF2ZSBsaW5nZXJlZCBhd2hpbGUgYW5kIHNhaWQ=,UG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==,QW5kIHRob3VnaHQgYmVmb3JlIEkgaGFkIGRvbmU=,T2YgYSBtb2NraW5nIHRhbGUgb3IgYSBnaWJl,VG8gcGxlYXNlIGEgY29tcGFuaW9u,QXJvdW5kIHRoZSBmaXJlIGF0IHRoZSBjbHViLA==,QmVpbmcgY2VydGFpbiB0aGF0IHRoZXkgYW5kIEk=,QnV0IGxpdmVkIHdoZXJlIG1vdGxleSBpcyB3b3JuOg==,QWxsIGNoYW5nZWQsIGNoYW5nZWQgdXR0ZXJseTo=,QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4=,VGhhdCB3b21hbidzIGRheXMgd2VyZSBzcGVudA==,SW4gaWdub3JhbnQgZ29vZCB3aWxsLA==,SGVyIG5pZ2h0cyBpbiBhcmd1bWVudA==,VW50aWwgaGVyIHZvaWNlIGdyZXcgc2hyaWxsLg==,V2hhdCB2b2ljZSBtb3JlIHN3ZWV0IHRoYW4gaGVycw==,V2hlbiB5b3VuZyBhbmQgYmVhdXRpZnVsLA==,U2hlIHJvZGUgdG8gaGFycmllcnM/,VGhpcyBtYW4gaGFkIGtlcHQgYSBzY2hvb2w=,QW5kIHJvZGUgb3VyIHdpbmdlZCBob3JzZS4=,VGhpcyBvdGhlciBoaXMgaGVscGVyIGFuZCBmcmllbmQ=,V2FzIGNvbWluZyBpbnRvIGhpcyBmb3JjZTs=,SGUgbWlnaHQgaGF2ZSB3b24gZmFtZSBpbiB0aGUgZW5kLA==,U28gc2Vuc2l0aXZlIGhpcyBuYXR1cmUgc2VlbWVkLA==,U28gZGFyaW5nIGFuZCBzd2VldCBoaXMgdGhvdWdodC4=,VGhpcyBvdGhlciBtYW4gSSBoYWQgZHJlYW1lZA==,QSBkcnVua2VuLCB2YWluLWdsb3Jpb3VzIGxvdXQu,SGUgaGFkIGRvbmUgbW9zdCBiaXR0ZXIgd3Jvbmc=,VG8gc29tZSB3aG8gYXJlIG5lYXIgbXkgaGVhcnQs,WWV0IEkgbnVtYmVyIGhpbSBpbiB0aGUgc29uZzs=,SGUsIHRvbywgaGFzIHJlc2lnbmVkIGhpcyBwYXJ0,SW4gdGhlIGNhc3VhbCBjb21lZHk7,SGUsIHRvbywgaGFzIGJlZW4gY2hhbmdlZCBpbiBoaXMgdHVybiw=,VHJhbnNmb3JtZWQgdXR0ZXJseTo=,QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4="
strings= strings.split(",")
pt= strings[0].decode('base64')
key=urandom(16)
nonce=""
for i in range(8):
	nonce=nonce+chr(0)
print ctr_encrypt(pt,key,nonce,16)