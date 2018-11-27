
def pad_check(pt):
	pad = pt[-1]
	for i in range(1,ord(pad)):
		if (pt[-i] != pad):
			return False
	return True

print (pad_check("ICE ICE BABY\x04\x04\x04\x04"))
print (pad_check("ICE ICE BABY\x05\x05\x05\x04"))
print (pad_check("ICE ICE BABY\x05\x05\x05\x05\x05"))
