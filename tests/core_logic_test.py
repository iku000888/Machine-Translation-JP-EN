# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_dao as dao
import mac_tran_core_logic as core

class TestCoreLogics(unittest.TestCase):
   
   #assert that words contained in the given sntc
   #can be identified, at least for most of the time.
   def test_attempt_word_retrieval_en(self):
      dao.delete_word_tbl()
      self.setup_data()
      w_ids=core.attempt_word_retrieval(u"I am going to\
         retrieve words that this sentence contains.")
      #print w_ids
      #for wid in w_ids:
      #   print dao.get_word_pair_by_id(wid)
      self.assertEqual(len(w_ids),11)
   def test_attempt_word_retrieval_jp(self):
      """
      Becauese Japanese sentences do not separate words by
      white space, the probability to retrieve all words is
      low, so only assert greater than 7.
      """
      dao.delete_word_tbl()
      self.setup_data()
      w_ids=core.attempt_word_retrieval(u"私はこれからこの\
            文に含まれる単語を取得する。")
      #print w_ids
      #for wid in w_ids:
      #   print dao.get_word_pair_by_id(wid)
      self.assertGreater(len(w_ids),7)
   def test_attempt_word_retrieval_dirty(self):
      dao.delete_word_tbl()
      self.setup_data()
      dirty_dict = self.setup_noise()
      input_sntc=u"I am going to "\
         "retrieve words that this sentence contains."
      w_ids=core.attempt_word_retrieval(input_sntc)
      w_ids=core.filter_retrieved_words(w_ids,input_sntc)
      #asser that the injected 'dirty data' is not included
      #in the results.
      for wid in w_ids:
         pair = dao.get_word_pair_by_id(wid)
         self.assertFalse(pair[0] in dirty_dict.keys())
         self.assertFalse(pair[1] in dirty_dict.values())
   def setup_data(self):
      pairs = dict()
      pairs["I"        ]=u"私"
      pairs["am"       ]=u"は"
      pairs["going"    ]=u"これから"
      pairs["to"       ]=u"を"
      pairs["retrieve" ]=u"取得する"
      pairs["words"    ]=u"単語"
      pairs["that"     ]=u"が"
      pairs["this"     ]=u"この"
      pairs["sentence" ]=u"文"
      pairs["contains"]=u"含む"
      pairs["."        ]=u"。"
      for k,v in pairs.iteritems():
         dao.insert_word_pair(k,v)
   def setup_noise(self):
      """
      To test for scenarios with dirty data,
      add random words that contain similar characters
      used in the test cases, used to confuse the logic.
      """
      pairs = dict()
      pairs["igloo"    ]=u"私たちは"
      pairs["game"     ]=u"はばたく"
      pairs["gang"     ]=u"からす"
      pairs["two"      ]=u"わをん"
      pairs["reveal"   ]=u"するめ"
      pairs["birds"    ]=u"単車"
      pairs["thanks"   ]=u"がらす"
      pairs["thus"     ]=u"このみ"
      pairs["senate"   ]=u"文学"
      pairs["coconuts" ]=u"含有"
      for k,v in pairs.iteritems():
         dao.insert_word_pair(k,v)
      return pairs
if __name__ == '__main__':
    unittest.main()
