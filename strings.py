import codecs

freqs = {
'a': 0.0651738,
'b': 0.0124248,
'c': 0.0217339,
'd': 0.0349835,
'e': 0.1041442,
'f': 0.0197881,
'g': 0.0158610,
'h': 0.0492888,
'i': 0.0558094,
'j': 0.0009033,
'k': 0.0050529,
'l': 0.0331490,
'm': 0.0202124,
'n': 0.0564513,
'o': 0.0596302,
'p': 0.0137645,
'q': 0.0008606,
'r': 0.0497563,
's': 0.0515760,
't': 0.0729357,
'u': 0.0225134,
'v': 0.0082903,
'w': 0.0171272,
'x': 0.0013692,
'y': 0.0145984,
'z': 0.0007836,
' ': 0.1918182
}

def hex_to_b64(hex_str):
	return codecs.encode(codecs.decode(hex_str, encoding='hex'), encoding='base64')

def score_english(str):
	score = 0
	for char in str:
		char = chr(char).lower()
		if char in freqs:
			score += freqs[char]
	return score

def reverse_dict(dictionary):
	return dict(zip(dictionary.values(), dictionary.keys()))

def get_letter_freqs(str):
	counts = {}
	non_chars = 0
	total = 0
	for char in str:
		if char.isalpha():
			if char.lower() in counts.keys():
				counts[char.lower()] += 1
			else:
				counts[char.lower()] = 1
			total += 1
		else:
			non_chars += 1
	freqs = {}
	non_chars /= total
	for char in counts.keys():
		freqs[char] = counts[char] / total
	return freqs, non_chars

if __name__ == '__main__':
	print(score_english('this seems like an English sentence'))
	print(score_english('rwazreyugbijmpokjnhubigvtfcdxseyuyibhu'))
