# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import machine_translation as mc

class TestSearchWordFromChunk(unittest.TestCase):
   
   def test_chunk_srch_en(self):
      mc.delete_word_tbl()
      mc.insert_word_pair("human","人間")
      result = mc.word_having_chunk("hu")
      print result
      self.assertTrue(True)
#input_str="人"
#print mc.word_having_chunk(input_str)
#print "reverse=",mc.random_reverse_split(input_str)

if __name__=='__main__':
   unittest.main()
