# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:40:21 2023

@author: prava
"""

import matplotlib.pyplot as plt
text =  "EBIIL TLOIA VMYM WBKIXQB QVVL"
alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# "E," "T," "A," "O," "I," "N," "S," "H," "R," and "D."
frequencies = {}
for x in alphabet:
    frequencies[x] = text.count(x)
    
plt.bar(frequencies.keys(), frequencies.values())
print(frequencies)
x = max(frequencies.items(), key = lambda x: x[1])
print(x)


def decode(text, alphabet, mode) :
  plain_list = []
  letters = ["E", "T" ,"A", "O", "I", "N" ,"S", "H", "R", "D"]
  cracked_list = []
  for letter in letters:
    key = alphabet.index(letter) - alphabet.index(mode)  
    decode_text = ''
    for x in text:
      decode_letter = alphabet[(alphabet.index(x)+key)%len(alphabet)]
      decode_text += decode_letter
    cracked_list.append(decode_text)
  return cracked_list

print(decode(text, alphabet, x[0]))
