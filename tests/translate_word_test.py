# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_dao as dao

class TestWordTranslation(unittest.TestCase):
   def test_english_to_japanese(self):
      dao.delete_word_tbl()
      en_input = "human"
      jp_input = u"人間" #need the u prefix to declare utf-8
      dao.insert_word_pair(en_input,jp_input)
      result = dao.translate_word("EN2JP",en_input)
      self.assertEqual(result, jp_input)

   def test_japanese_to_english(self):
      dao.delete_word_tbl()
      en_input = "human"
      jp_input = u"人間" #need the u prefix to declare utf-8
      dao.insert_word_pair(en_input,jp_input)
      result = dao.translate_word("JP2EN",jp_input)
      self.assertEqual(result, en_input)
#   """
#   Test for multiple words containing the input chunk.
#   Ensure that what gets put in, is retrieved by verifying
#   the number of elements.
#   """
#   def test_chunk_srch_multiple_en(self):
#      dao.delete_word_tbl()
#      pairs = dict()
#      pairs["living"    ]=u"生活する"
#      pairs["invited"   ]=u"招待される"
#      pairs["involved"  ]=u"関わる"
#      pairs["indeed"    ]=u"そのとおり"
#      pairs["intention" ]=u"想定"
#      pairs["initiation"]=u"開始"
#      pairs["nicotine"  ]=u"ニコチン"
#      pairs["bin"       ]=u"ゴミ箱"
#      for en_word in pairs.keys():
#         dao.insert_word_pair(en_word,pairs[en_word])
#      list_stuff = list()
#      result = dao.word_having_chunk("in")
#      for wid in result:
#         retrieved_pair=dao.get_word_pair_by_id(int(wid))
#         list_stuff.append(retrieved_pair)
#      self.assertEqual(len(list_stuff),8)
#         #self.assertEqual(jp_input,retrieved_pair[1])

if __name__=='__main__':
   unittest.main()
