"""
Leveraging the dao and util, produce useful results.
"""
import mac_tran_dao as dao
import mac_tran_utils as util


def attempt_word_retrieval(sntc):
   """
   given a sentence, 'attempt' to identify the words that
   are included in the sentence, by splitting the sentence
   into arbitrary chunks, and hoping it would partially
   match a word.
   """
   chunks_forward = util.random_split(sntc)
   chunks_backwards = util.random_reverse_split(sntc)
   word_ids = set()
   for chunk in chunks_forward:
      word_ids |= set(dao.word_having_chunk(chunk))
   for chunk in chunks_backwards:
      word_ids |= set(dao.word_having_chunk(chunk))
   return word_ids

def filter_retrieved_words(word_ids,sntc):
   """
   After attempting word retrieval, filter words
   that are not included in the original sentence.
   """
   return word_ids
