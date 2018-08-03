import binascii
from strings import score_english

def fixed_xor(str1, str2):
	if len(str1) == len(str2):
		enc = b""
		for i in range(len(str1)):
			enc += bytes([str1[i] ^ str2[i]])
		return enc
	return None

def single_byte_xor(str1, b):
	enc = b""
	for i in range(len(str1)):
		enc += bytes([str1[i] ^ b])
	return enc

def repeating_xor(str1, key):
	enc = b""
	for i in range(len(str1)):
		enc += bytes([str1[i] ^ key[i % len(key)]])
	return enc

if __name__ == '__main__':
	str1 = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
	key = b'ICE'
	enc = repeating_xor(str1, key)
	print(binascii.hexlify(enc))
