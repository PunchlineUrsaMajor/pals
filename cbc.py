import aes_ecb
import xor
import base64

def cbc_enc(text, key, iv, blocksize):
	if len(text) != 0:
		x = xor.fixed_xor(text[:blocksize], iv)
		enc = aes_ecb.enc_aes_ecb(x, key)
		return cbc_enc(text[blocksize:], key, enc, blocksize)
	return iv

def cbc_dec(ciphertext, key, iv, blocksize):
	if len(ciphertext) != 0:
		dec = aes_ecb.dec_aes_ecb(ciphertext[:blocksize], key)
		x = xor.fixed_xor(dec, iv)
		return x + cbc_dec(ciphertext[blocksize:], key, ciphertext[:blocksize], 16)
	return b''

if __name__ == '__main__':
	key = b'YELLOW SUBMARINE'
	text = b'this is a test!!'
	iv = bytes([0] * 16)
	with open('10.txt', 'r') as f:
		data = base64.b64decode(f.read())
	print(cbc_dec(data, key, iv, 16))
