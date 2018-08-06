from Crypto.Cipher import AES
import base64
import binascii
import pad

def enc_aes_ecb(text, key):
	text = pad.pkcs7(text, len(key))
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.encrypt(text)

def dec_aes_ecb(text, key):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.decrypt(text)

if __name__ == '__main__':
	enc = enc_aes_ecb(b'this is a test!!', b'YELLOW SUBMARINE')
	print(dec_aes_ecb(enc, b'YELLOW SUBMARINE'))
