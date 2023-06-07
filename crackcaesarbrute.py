alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def crack_caesar(ciph_text, aplhabet):
    cracked = []
    for key in range(len(alphabet)):
        x = ''
        for letter in ciph_text:
            x += alphabet[(alphabet.index(letter)-key)%len(alphabet)]
        cracked.append(x)
    return cracked

listt = crack_caesar('YJMM YO', alphabet)
print(listt)
print(listt.index('CORRECT'))

