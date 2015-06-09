# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_utils as util

class TestTempletization(unittest.TestCase):
   """
   Test for multiple words containing the input chunk.
   Ensure that what gets put in, is retrieved by verifying
   the number of elements.
   """
   def test_templetization_en(self):
      sntc = "I am alive today."
      pairs = dict()
      pairs[u"I"    ]="$<1>"
      pairs[u"am"   ]="$<2>"
      pairs[u"alive"]="$<3>"
      pairs[u"today"]="$<4>"
      pairs[u"."]="$<5>"
      returned_val = util.templetize_sentence(sntc,pairs)
      self.assertEqual("$<1> $<2> $<3> $<4>$<5>",returned_val)
if __name__=='__main__':
   unittest.main()
