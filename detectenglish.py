# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:44:18 2023

@author: prava
"""

#import nltk

#nltk.download('words')

from nltk.corpus import words
english_words = words.words()

text = ' GUBYQTF'
alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


  
  

def decode(text, alphabet):
  listt = []
  for key in range(len(alphabet)):
    stri = ''
    for x in text:
      decode_letter = alphabet[(alphabet.index(x)-key)%len(alphabet)]
      stri += decode_letter
    listt.append(stri)
  return listt


listtt = decode(text, alphabet)



for element in listtt :
  element = element.lower()
  res = element.split(' ')
  if set(res).issubset(set(english_words)):
    print(element)

