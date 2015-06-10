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
      pairs["living"    ]=u"生活する"
      pairs["invited"   ]=u"招待される"
      pairs["involved"  ]=u"関わる"
      pairs["indeed"    ]=u"そのとおり"
      pairs["intention" ]=u"想定"
      pairs["initiation"]=u"開始"
      pairs["nicotine"  ]=u"ニコチン"
      pairs["bin"       ]=u"ゴミ箱"
      for k,v in pairs.iteritems():
         dao.insert_word_pair(k,v)
if __name__ == '__main__':
    unittest.main()
