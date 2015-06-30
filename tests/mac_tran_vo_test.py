# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_vo as vo 

class TestMacTranVo(unittest.TestCase):
   def test_setter_getters_en(self):
      test_vo = vo.MacTranVo()
      test_vo.set_sentence(u"hello, can you hear me?")
      self.assertEqual(test_vo.get_sentence(),
                        u"hello, can you hear me?") 
   
   def test_setter_getters_jp(self):
      test_vo = vo.MacTranVo()
      test_vo.set_sentence(u"こんにちは、聞こえますか?")
      self.assertEqual(test_vo.get_sentence(),
                        u"こんにちは、聞こえますか?") 
      
if __name__=='__main__':
   unittest.main()
