output_len=20
s="YELLOW SUBMARINE"
tmp = len(s)
padding_len = output_len - tmp
for i in range(padding_len):
	s = s + chr(padding_len)

print (s)