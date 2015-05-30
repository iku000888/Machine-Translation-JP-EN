import unittest
import sys
sys.path.append('../src/')
import mac_tran_utils as util
      
class TestRandomSplittingMethods(unittest.TestCase):
   
   def test_forward(self):
      input_str="This is a string to be split,\
            please take a look at what happens"
      print "forward=",util.random_split(input_str)
      print "reverse=",util.random_reverse_split(input_str)  
      self.assertTrue(True)      
 
if __name__=='__main__':
   unittest.main()
