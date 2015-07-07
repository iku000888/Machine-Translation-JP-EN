# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_dao as dao
import mac_tran_core_logic as core

class TestRetrieveSentenceHavingWordsIn(unittest.TestCase):
   def test_attempt_sntc_retrieval_dirty_jp(self):
      dao.delete_word_tbl()
      self.setup_data()
      dirty_dict = self.setup_noise()
      input_sntc=u"私はこれからこの"\
            u"文に含まれる単語を取得する。"
      w_ids=core.attempt_word_retrieval(input_sntc)
      w_ids=core.filter_retrieved_words(w_ids,input_sntc)
      #asser that the injected 'dirty data' is not included
      #in the results.
      for wid in w_ids:
         pair = dao.get_word_pair_by_id(wid)
         self.assertFalse(pair[0] in dirty_dict.keys())
         self.assertFalse(pair[1] in dirty_dict.values())
   def setup_data(self):
      word_pairs = dict()
      word_pairs["I"        ]=u"私"
      word_pairs["am"       ]=u"は"
      word_pairs["going"    ]=u"これから"
      word_pairs["to"       ]=u"を"
      word_pairs["retrieve" ]=u"取得する"
      word_pairs["words"    ]=u"単語"
      word_pairs["that"     ]=u"が"
      word_pairs["this"     ]=u"この"
      word_pairs["sentence" ]=u"文"
      word_pairs["contains"]=u"含む"
      word_pairs["."        ]=u"。"
      for k,v in word_pairs.iteritems():
         dao.insert_word_pair(k,v)
      sntc_pairs = dict()
      sntc_pairs["I am going to retrieve words that this sentence contains" ]=u"私はこれからこの"\
            u"文に含まれる単語を取得する。"
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
