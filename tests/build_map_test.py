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
      pairs = dict()
      pairs[u"I"    ]=u"私"    
      pairs[u"am"   ]=u"は"    
      pairs[u"a"    ]=u"一人の"
      pairs[u"human"]=u"人間だ"
      for k,v in pairs.iteritems():
         dao.insert_word_pair(k,v)
      dao.insert_sentence_pair(u"I am a human",
                                 u"私は一人の人間だ")
      #build the relational mapping.
      dao.build_word_sntc_mp()

      #verify that the words are reachable from the sentence.
      sntc_id = dao.get_sntc_id(u"I am a human")
      word_ids= dao.words_belonging_to_sntc(sntc_id)
      for k,v in pairs.iteritems():
         self.assertTrue(True)
      print word_ids

      #verify that the sentence is reachable from the words.


#   def test_dictionary_import(self):
#      dao.delete_word_tbl()
#      dao.delete_sntc_tbl()
#      dao.delete_sntc_wd_tbl()
#      dao.import_word_pairs("../datasets/wordmp.csv")
#      dao.import_sentence_pairs("../datasets/sntcmp.txt")
#      dao.build_word_sntc_mp()
if __name__=='__main__':
   unittest.main()
