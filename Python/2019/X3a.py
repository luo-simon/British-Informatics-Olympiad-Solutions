import itertools

inp = input('> ').split(' ')
length = int(inp[0])
start = inp[1]

def check_order(string):
	if len(string) == 1:
		return 0
	#count = 0
	current_index = alphabet.index(string[0])
	for char in string:
		if alphabet.index(char) > current_index:
			return 1 + check_order(string[string.index(char):])
			#current_index = alphabet.index(char)
		#if count >= 2:
			#return False
	return check_order(string[1:])

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

chars = [char for char in alphabet[:length] if char not in start]

blockchains = []
num_blockchains = 0

for i in itertools.permutations(chars, len(chars)):
	s = start + ''.join(i)
	if check_order(s):
		blockchains.append(s)
		num_blockchains += 1

print(blockchains)
print(num_blockchains)
print






