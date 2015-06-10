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
   print sntc
   word_ids = list()
   return word_ids
