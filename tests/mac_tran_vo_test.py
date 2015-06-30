# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_vo as vo 

class TestMacTranVo(unittest.TestCase):
   def test_setter_getters_en(self):
      test_vo = vo.MacTranVo()
      test_vo.set_sentence("hello, can you hear me?")
      self.assertEqual(test_vo.get_sentence(),
                        "hello, can you hear me?") 
      
if __name__=='__main__':
   unittest.main()
