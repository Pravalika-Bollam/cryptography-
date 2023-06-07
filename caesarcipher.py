alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#alphabet contains 27 letters , starting with a whitespace given 0, a, 1 so on
key = 238

#find() returns -1 if not found, index() raises value error
#both are case senisitive
#use .lower() or .upper() to make it insensitive , as per the alphabet case

def caesar_encrypt(plain_text, key, alphabet):
    ciph = ''
    for x in plain_text:
        ciph = ciph + alphabet[(alphabet.index(x)+key)%len(alphabet)]
    return ciph

def caesar_decrypt(cipher_text, key, alphabet):
    plain = ''
    for x in cipher_text:
        plain += alphabet[(alphabet.index(x)-key)%len(alphabet)]
    return plain

x = caesar_encrypt('CORRECT',key, alphabet)
print(x)
y = caesar_decrypt(x, key, alphabet)
print(y)
