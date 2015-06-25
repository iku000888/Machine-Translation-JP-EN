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
   def __init__(self,string, lang):
      self.string = string
      self.lang = lang

   def print_self(self):
      print self.string
      print self.lang
