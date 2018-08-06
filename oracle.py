import cbc
import aes_ecb
import random
import os
import pad
import base64

unknown_text = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK"""

def encryption_oracle(text):
	key = generate_key(16)
	text = generate_key(random.randint(5, 10)) + text + generate_key(random.randint(5, 10))
	text = pad.pkcs7(text, 16)
	if random.random() < .5:
		return aes_ecb.enc_aes_ecb(text, key)
	else:
		return cbc.cbc_enc(text, key, generate_key(16), 16)

def generate_key(size):
	return os.urandom(size)

KEY = generate_key(16)

def append_oracle(text):
	text += base64.b64decode(unknown_text)
	text = pad.pkcs7(text, 16)
	blocks = [text[i: i + 16] for i in range(0, len(text), 16)]
	enc = b''
	for block in blocks:
		enc += aes_ecb.enc_aes_ecb(block, KEY)
	return enc

if __name__ == '__main__':
	print(append_oracle(b'this is a test'))
	print(append_oracle(b'this is a test'))
