# -*- coding: utf-8 -*-
import sys
sys.path.append('../src/')
import machine_translation as mc
input_str="人"
print mc.word_having_chunk(input_str)
#print "reverse=",mc.random_reverse_split(input_str)
