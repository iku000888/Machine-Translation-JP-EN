# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_dao as dao

class TestSearchWordFromChunk(unittest.TestCase):
   def test_chunk_srch_en(self):
      dao.delete_word_tbl()
      en_input = "human"
      jp_input = u"人間" #need the u prefix to declare utf-8
      dao.insert_word_pair(en_input,jp_input)
      result = dao.word_having_chunk("hu")[0]
      retrieved_pair= dao.get_word_pair_by_id(int(result))
      self.assertEqual(en_input, retrieved_pair[0])
      self.assertEqual(jp_input,retrieved_pair[1])

   def test_chunk_srch_jp(self):
      dao.delete_word_tbl()
      en_input = "human"
      jp_input = u"人間" #need the u prefix to declare utf-8
      dao.insert_word_pair(en_input,jp_input)
      result = dao.word_having_chunk("人")[0]
      retrieved_pair= dao.get_word_pair_by_id(int(result))
      self.assertEqual(en_input, retrieved_pair[0])
      self.assertEqual(jp_input,retrieved_pair[1])

   def test_chunk_srch_multiple_en(self):
      dao.delete_word_tbl()
      dao.insert_word_pair("living",u"生活する")
      dao.insert_word_pair("invited",u"招待される")
      dao.insert_word_pair("involved",u"関わる")
      dao.insert_word_pair("indeed",u"そのとおり")
      dao.insert_word_pair("intention",u"想定")
      dao.insert_word_pair("initiation",u"開始")
      dao.insert_word_pair("nicotine",u"ニコチン")
      dao.insert_word_pair("bin",u"ゴミ箱")
      result = dao.word_having_chunk("in")
      print result
      #retrieved_pair= dao.get_word_pair_by_id(int(result))
      #self.assertEqual(en_input, retrieved_pair[0])
      #self.assertEqual(jp_input,retrieved_pair[1])

if __name__=='__main__':
   unittest.main()
