# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_dao as dao

class TestBuildSntcWordMp(unittest.TestCase):
   def test_dictionary_import(self):
      dao.delete_word_tbl()
      dao.delete_sntc_tbl()
      dao.delete_sntc_wd_tbl()
      dao.import_word_pairs("../datasets/wordmp.csv")
      dao.import_sentence_pairs("../datasets/sntcmp.txt")
      dao.build_word_sntc_mp()
if __name__=='__main__':
   unittest.main()
