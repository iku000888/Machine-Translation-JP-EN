# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_dao as dao
import mac_tran_core_logic as core

class TestCoreLogics(unittest.TestCase):
   def test_attempt_word_retrieval(self):
      dao.delete_word_tbl()
      self.setup_data()
      core.attempt_word_retrieval(u"I am going to retrieve"\
          u" words that this sentence contains.")

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
      pairs["containts"]=u"含む"
      pairs["."        ]=u"。"
      for k,v in pairs.iteritems():
         dao.insert_word_pair(k,v)
if __name__ == '__main__':
    unittest.main()
