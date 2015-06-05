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
   
   def test_japanese_to_english_arg_err(self):
      dao.delete_word_tbl()
      en_input = "human"
      jp_input = u"人間" #need the u prefix to declare utf-8
      dao.insert_word_pair(en_input,jp_input)
      with self.assertRaises(KeyError):
         self.assertRaises(dao.translate_word("JPN",jp_input))
   
   def test_japanese_to_english_not_found(self):
      dao.delete_word_tbl()
      en_input = "human"
      jp_input = u"人間" #need the u prefix to declare utf-8
      dao.insert_word_pair(en_input,jp_input)
      with self.assertRaises(TypeError):
         self.assertRaises(dao.translate_word("JP2EN",u"灰"))

if __name__=='__main__':
   unittest.main()
