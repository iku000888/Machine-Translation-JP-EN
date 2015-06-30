class MacTranVo():
   """
   This class should package data and access methods relavant
   to the logic part. As of now, I am imagining the following attributes:
      -The sentence it self.
      -The string's meta data
         -The detected template <i's> and mapping to the words contained in the
            sentence
      -List of candidate strings fetched from the DB, given by the DAO.
      -Some fuzzy-ish logic to translate the 
       sentence using the above items as ingredients

      
   """
   def __init__(self):

   def set_sentence(self,sentence):
      self.sentence=sentence

   def get_sentence(self):
      return self.sentence

   def set_detected_template(self,template):
      self.template = template

   def get_detected_template(self):
      return self.template

   def get_candidate_strings(self):
      return self.candidate_strings
   
   def add_candidate_string(self, string):
      self.candidate_strings.add(string)
