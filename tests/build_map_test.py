# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_dao as dao

class TestBuildSntcWordMp(unittest.TestCase):
   def test_dictionary_simple(self):
      dao.delete_word_tbl()
      dao.delete_sntc_tbl()
      dao.delete_sntc_wd_tbl()
      dao.insert_word_pair(u"I",u"私")
      dao.insert_word_pair(u"am",u"は")
      dao.insert_word_pair(u"a",u"一人の")
      dao.insert_word_pair(u"human",u"人間だ")
      dao.insert_sentence_pair(u"I am a human",
                                 u"私は一人の人間だ")
      dao.build_word_sntc_mp()
      dao.words_belonging_to_sntc(21)
#   def test_dictionary_import(self):
#      dao.delete_word_tbl()
#      dao.delete_sntc_tbl()
#      dao.delete_sntc_wd_tbl()
#      dao.import_word_pairs("../datasets/wordmp.csv")
#      dao.import_sentence_pairs("../datasets/sntcmp.txt")
#      dao.build_word_sntc_mp()
if __name__=='__main__':
   unittest.main()
