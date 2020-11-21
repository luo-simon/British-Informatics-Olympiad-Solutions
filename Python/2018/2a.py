n, word = input('> ').split()
n = int(n)

alphabet = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

def create_cipher():
    cipher = []
    index = 0
    while len(alphabet) > 0:
        index += n-1
        index = index % len(alphabet) # equivalent to i %= len(alphabet)
        cipher.append(alphabet[index])
        alphabet.pop(index)
    return cipher

def encrypt(word, cipher):
    encrypted = ''
    alphabet = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    for c in word:
        index = alphabet.index(c)
        encrypted += cipher[index]
        cipher.extend(cipher[:1])
        cipher = cipher[1:]
    return encrypted


cipher = create_cipher()
print("".join(cipher[:6]))
print(encrypt(word, cipher))
