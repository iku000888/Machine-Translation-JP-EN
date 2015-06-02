# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import machine_translation as mc

class TestSearchWordFromChunk(unittest.TestCase):
   def test_chunk_srch_en(self):
      mc.delete_word_tbl()
      en_input = "human"
      jp_input = u"人間" #need the u prefix to declare utf-8
      mc.insert_word_pair(en_input,jp_input)
      result = mc.word_having_chunk("hu")[0]
      retrieved_pair= mc.get_word_pair_by_id(int(result))
      self.assertEqual(en_input, retrieved_pair[0])
      print jp_input, retrieved_pair[1]
      self.assertEqual(jp_input,retrieved_pair[1])

if __name__=='__main__':
   unittest.main()
