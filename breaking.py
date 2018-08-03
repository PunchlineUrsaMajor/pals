import strings
import xor
import binascii
import base64

def distance(str1, str2):
	if len(str1) == len(str2):
		distance = 0
		for i in range(0, len(str1)):
			if str1[i] != str2[i]:
				a = '{0:08b}'.format(str1[i])
				b = '{0:08b}'.format(str2[i])
				for j in range(len(a)):
					if a[j] != b[j]:
						distance += 1
	return distance

def break_single_byte_xor(text):
	def key(p):
		return strings.score_english(p[1])
	return max([(i, xor.single_byte_xor(text, i)) for i in range(0, 256)], key=key)

def transpose(mat):
	t_mat = [b"" for i in range(len(mat[0]))]
	for block in mat:
		for i in range(len(block)):
			try:
				t_mat[i] += bytes([block[i]])
			except Exception:
				pass
	return t_mat

def break_repeating_xor(text, min_len=10, max_len=40):
	dists = {}
	for i in range(min_len, max_len + 1):
		first = text[:i]
		second = text[i:i * 2]
		dist = distance(first, second) / i
		dists[i] = dist
	rev_dists = dict(zip(dists.values(), dists.keys()))
	smallest_dist = sorted(dists.values())
	keysizes = [rev_dists[dist] for dist in smallest_dist]
	scores = {}
	for keysize in keysizes:
		blocks = [text[i:i + keysize] for i in range(0, len(text) - (len(text) % keysize), keysize)]
		blocks.append(text[len(text) - (len(text) % keysize):])
		blocks = transpose(blocks)
		key = b""
		for block in blocks:
			key_part, _ = break_single_byte_xor(block)
			key += bytes([key_part])
		dec = xor.repeating_xor(text, key)
		scores[keysize] = (strings.score_english(dec), key)
	return max([(scores[i], i) for i in scores.keys()])

if __name__ == '__main__':
	with open('6.txt', 'r') as f:
		data = base64.b64decode(f.read())
		print(break_repeating_xor(data))
