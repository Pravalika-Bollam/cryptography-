# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:59:04 2023

@author: prava
"""

alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plain_text = 'Hello'
key = 'key'

def vigene_encrypt(alphabet, plain_text, key):
  plain_text = plain_text.upper()
  key = key.upper()
  ct= ''
  if len(key)<len(plain_text):
    for i in range(len(plain_text)-len(key)):
      key += key[i]
  print(key)
  m = 0
  for x in plain_text:
    ct += alphabet[(alphabet.index(x)+ alphabet.index(key[m]))%len(alphabet)]
    m+=1
  return ct
  

CT = vigene_encrypt(alphabet, plain_text, key)


def vigener_decrypt(alphabet, cipher_text, key):
  cipher_text = cipher_text.upper()
  key =key.upper()
  pt= ''
  if len(key)<len(cipher_text):
    for i in range(len(cipher_text)-len(key)):
      key += key[i]
  m = 0
  for x in cipher_text:
    pt += alphabet[(alphabet.index(x)-alphabet.index(key[m]))%len(alphabet)]
    m +=1
  return pt

print(CT)
print(vigener_decrypt(alphabet, CT, key))
  
    
  
  
  


  
  