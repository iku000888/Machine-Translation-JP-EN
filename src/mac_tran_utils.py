import random
# -*- coding: utf-8 -*-

def random_split(str_to_split):
   splitted_list = list()
   while len(str_to_split)>=1:
      len_chunk=1+int(.35*round(random.random()\
      *len(str_to_split)))
      chunk=str_to_split[0:len_chunk]
      splitted_list.append(chunk)
      str_to_split=str_to_split[len_chunk:len(str_to_split)]
   return splitted_list

def random_reverse_split(str_to_split):
   rand_reversed_str=random_split(str_to_split[::-1])
   fix_chunks = list()
   for chunk in rand_reversed_str:
      fix_chunks.append(chunk[::-1])
   return fix_chunks
    
def balanced_split(str_to_split):
   print str_to_split
   return

def templetize_sentence(sntc,word_dict):
   """
   Eventually, given three things:
      1. input format = [$<1>$<2> ...],
      2. values [$<1>="some word" $<2>="some other word"...]
      3. specified output format [$<2> $<1> ...]
   Return third item with values fetched from the DB.
   
   As a prototype, given a set of already known words,
   replace them with '$<i>'s.
   """
   templetized_sntc = sntc
   for word,param in word_dict.iteritems():
      templetized_sntc = templetized_sntc.replace(word,param)
   return templetized_sntc
