"""
Leveraging the dao and util, produce useful results.
"""
import mac_tran_dao as dao
import mac_tran_utils as util


def attempt_word_retrieval(sntc):
   """
   given a sentence, 'attempt' to identify the words that
   are included in the sentence by splitting the sentence
   into arbitrary chunks, and hoping it would partially
   match a word.
   """
   print "sntc = :", sntc
   chunks_forward = util.random_split(sntc)
   chunks_backwards = util.random_reverse_split(sntc)
   for chunk in chunks_forward:
      word_ids = dao.word_having_chunk(chunk)
      print chunk, word_ids
      for word_id in word_ids:
         print dao.get_word_pair_by_id(word_id)[0]
   for chunk in chunks_backwards:
      word_ids = dao.word_having_chunk(chunk)
      print chunk, word_ids
      for word_id in word_ids:
         print dao.get_word_pair_by_id(word_id)[0]
   word_ids = list()
   return word_ids
