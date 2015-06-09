# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_util as util

class TestSearchWordFromChunk(unittest.TestCase):
   """
   Test for multiple words containing the input chunk.
   Ensure that what gets put in, is retrieved by verifying
   the number of elements.
   """
   def test_chunk_srch_multiple_en(self):
      dao.delete_word_tbl()
      sntc = "I am alive today."
      pairs = dict()
      pairs[u"I"    ]="$<1>"
      pairs[u"am"   ]="$<2>"
      pairs[u"alive"]="$<3>"
      pairs[u"today"]="$<4>"
if __name__=='__main__':
   unittest.main()
