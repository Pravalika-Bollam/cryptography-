


#it is to be noted that using key value 2, then key value 5 is same as using key value 7 at once
#so multiple caesar encryptions doesnt work any better



ascii_text = ''

for i in range(256):
    ascii_text += chr(i)

def caesar_encrypt(plain_text, key, ascii_text):
    plain = ''
    for x in plain_text:
        plain += ascii_text[(ord(x)+key)%len(ascii_text)]
    return plain


def caesar_decrypt(cipher_text, key, ascii_text):
    ciph = ''
    for x in cipher_text:
        ciph += ascii_text[(ord(x)-key)%len(ascii_text)]
    return ciph

x = caesar_encrypt('ABC abc?.,<>', 3, ascii_text)
print(x)
print(caesar_decrypt(x, 3, ascii_text))


