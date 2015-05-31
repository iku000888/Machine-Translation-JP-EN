# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src/')
import mac_tran_utils as util
      
class TestRandomSplittingMethods(unittest.TestCase):
   """
   Ensure that no character is lost, 
   or no extraneous characters are added.
   """ 
   def test_forward(self):
      input_str="This is a string to be split,\
            please take a look at what happens"
      forward = util.random_split(input_str)
      result = ""
      for chunk in forward:
         result += chunk
      #print "forward=",util.random_split(input_str)
      #print "reverse=",util.random_reverse_split(input_str)  
      self.assertEqual(result,input_str)      
   
   """
   Ensure that no character is lost, 
   or no extraneous characters are added.
   """
   def test_backward(self):
      input_str="This is a string to be split,i"\
                "please take a look at what happens"
      reverse=util.random_reverse_split(input_str)[::-1]
      result = ""
      for chunk in reverse:
         result+=chunk
      #print result
      self.assertEqual(result,input_str)      

   """
   test that splitting also works for Japanese characters.
   """
   def test_forward_JA(self):
      input_str="これは分割される文字列です、\
                何が起こるか見ていてください"
      forward = util.random_split(input_str)
      result = ""
      for chunk in forward:
         result += chunk
      #print "forward=",util.random_split(input_str)
      #print "reverse=",util.random_reverse_split(input_str)  
      self.assertEqual(result,input_str)       
   
if __name__=='__main__':
   unittest.main()
