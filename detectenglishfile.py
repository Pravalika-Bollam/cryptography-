# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 18:53:46 2023

@author: prava
"""
with open("D:\downloads\cryptography\english_words.txt" , 'r') as word_file:
  contents = word_file.readlines()

new_contents = [content.rstrip() for content in contents]
#print(new_contents[:5])

def decode (text, alphabet):
  cracked_list = []
  for key in range(len(alphabet)):
    decode_string = ''
    for x in text:
      decode_text = alphabet[(alphabet.index(x)-key)%len(alphabet)]
      decode_string += decode_text
    cracked_list.append(decode_string)
  return cracked_list


final_string = decode('EQFGBRNQV', ' ABCDEFGHIJKLMNOPQRSTUVWXYZ')


for element in final_string:
  element = element.split(" ")
  if set(element).issubset(set(new_contents)):
    print(element)


