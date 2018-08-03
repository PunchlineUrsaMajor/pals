def pkcs7(text, blocksize):
	rem = len(text) % blocksize
	if rem != 0:
		pad = blocksize - rem
		text += bytes([pad]) * pad
	return text

if __name__ == '__main__':
	text = b'YELLOW SUBMARINE'
	print(pkcs7(text, 20))
