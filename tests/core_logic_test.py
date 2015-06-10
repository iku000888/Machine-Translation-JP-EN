import unittest
import sys
sys.path.append('../src/')
import mac_tran_dao as dao
import mac_tran_core_logic as core

class TestSearchWordFromChunk(unittest.TestCase):
   def test_chunk_srch_en(self):
      dao.delete_word_tbl()
      print "hello!"
if __name__ == '__main__':
    unittest.main()

