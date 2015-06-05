import mysql.connector
#codecs module is necessary for writng utf-8 chars to a file.
import codecs
#Credential informations stored as env. vars.
import os
# -*- coding: utf-8 -*-
import mac_tran_utils as util

"""
factored out connection informations.
Password, ID, and IP addresses are
stored as env. variables which in turn
are set in a script.
"""
def get_cnx():
   cnx = mysql.connector.connect(user=os.environ["MYSQLID"],
                             password=os.environ["MYSQLPW"],
                             host=os.environ["MYSQLIP"],
                             database='EN_JAP')
   return cnx

"""
clear the content of the table, mainly for unit test purposes.
"""
def delete_word_tbl():
   cnx = get_cnx()
   cursor = cnx.cursor()
   del_words = ("DELETE FROM word_mp")    
   cursor.execute(del_words)
   cnx.commit()
   cursor.close()
   cnx.close()
   return
"""
clear the content of the table, mainly for unit test purposes.
"""
def delete_sntc_tbl():
   cnx = get_cnx()
   cursor = cnx.cursor()
   del_words = ("DELETE FROM sentence_mp")    
   cursor.execute(del_words)
   cnx.commit()
   cursor.close()
   cnx.close()
   return
"""
clear the content of the table, mainly for unit test purposes.
"""
def delete_sntc_wd_tbl():
   cnx = get_cnx()
   cursor = cnx.cursor()
   del_words = ("DELETE FROM sentence_word_mp")    
   cursor.execute(del_words)
   cnx.commit()
   cursor.close()
   cnx.close()
   return
"""
Insert a pair of Enlish-Japanese
pair of a word into the table.
"""
def insert_word_pair(en_word,jp_word):
   cnx = get_cnx()
   cursor = cnx.cursor()
   add_word = ("INSERT INTO word_mp "
                  "(english_word, japanese_word) "
                  "VALUES (%s, %s)")
   data_word = (en_word,jp_word)   
   cursor.execute(add_word,data_word)
   cnx.commit()
   cursor.close()
   cnx.close()
   return
"""
dump every word pairs from the database,
as a csv file, into the file name provided in the
input argument.
"""
def export_word_pairs(outfile):
   #print outfile
   cnx = get_cnx()
   cursor = cnx.cursor()
   get_words = ("select * from word_mp;")
   cursor.execute(get_words)
   fo = codecs.open(outfile,"w","utf-8")
   for(word_id,english_word,japanese_word) in cursor:
      fo.write(u"{},{}".format(english_word,japanese_word)
      +u"\n")
   fo.close()
   cursor.close()
   cnx.close()
   return

def import_word_pairs(infile):
   #print outfile
   #does not call insert_word_pair because
   #intention is to import large volume, and
   #connecting every single time is a waste of time.
   cnx = get_cnx()
   cursor = cnx.cursor()
   pairs = open(infile,"r")
   for line in pairs.readlines():
      pair = line.rstrip("\n").split(",")
      if len(pair)!=2:
         print pair, "something wrong"
         continue
      en_word = pair[0]
      jp_word = pair[1]
      add_word = ("INSERT INTO word_mp "
                  "(english_word, japanese_word) "
                  "VALUES (%s, %s)")
      data_word = (en_word,jp_word)   
      cursor.execute(add_word,data_word)
   pairs.close()
   cnx.commit()
   cursor.close()
   cnx.close()
   return

def translate_word(direction,word):
   #map of translation directon to query used.
   #print "translating word..."
   dir_sql_map = {"EN2JP":"select japanese_word " 
                          "from word_mp " 
                          "where english_word=%s;",
                  "JP2EN":"select english_word " 
                          "from word_mp " 
                          "where japanese_word=%s;" }
   #print dir_sql_map 
   cnx = get_cnx()
   cursor = cnx.cursor()
   #print dir_sql_map[direction]
   mapped_query = (dir_sql_map[direction])
   data_word = (word,)
   #print word
   cursor.execute(mapped_query,data_word)
   translated_word = cursor.fetchone()[0]
   cursor.close()
   cnx.close()  
   return translated_word

def insert_sentence_pair(en_sntc,jp_sntc):
   cnx = get_cnx()
   cursor = cnx.cursor()
   add_sntc = ("INSERT INTO sentence_mp "
                  "(english_sntc, japanese_sntc) "
                  "VALUES (%s, %s)")
   data_sntc = (en_sntc,jp_sntc)   
   cursor.execute(add_sntc,data_sntc)
   cnx.commit()
   cursor.close()
   cnx.close()
   return

def export_sentence_pairs(outfile):
   #print outfile
   cnx = get_cnx()
   cursor = cnx.cursor()
   get_sentences = ("select * from sentence_mp;")
   cursor.execute(get_sentences)
   fo = codecs.open(outfile,"w","utf-8")
   for(sntc_id,english_sntc,japanese_sntc) in cursor:
      fo.write(u"{}><{}".format(english_sntc,japanese_sntc)
                                                   +u"\n");
   fo.close()
   cursor.close()
   cnx.close()
   return

def import_sentence_pairs(infile):
   #print outfile
   #does not call insert_word_pair because
   #intention is to import large volume, and
   #connecting every single time is a waste of time.
   cnx = get_cnx()
   cursor = cnx.cursor()
   pairs = open(infile,"r")
   add_sntc = ("INSERT INTO sentence_mp "
               "(english_sntc, japanese_sntc) "
               "VALUES (%s, %s)")
   for line in pairs.readlines():
      pair = line.rstrip("\n").split("><")
      en_sntc = pair[0]
      jp_sntc = pair[1]
      data_sntc = (en_sntc,jp_sntc)   
      cursor.execute(add_sntc,data_sntc)
   pairs.close()
   cnx.commit()
   cursor.close()
   cnx.close()
   return

def print_all_words():
   cnx = get_cnx()
   cursor = cnx.cursor()
   add_sntc = ("select * from word_mp;")
   cursor.execute(add_sntc)
   for (wid,en_wd,jp_wd) in cursor:
      print wid, en_wd, jp_wd 
   cnx.commit()
   cursor.close()
   cnx.close()
   return
"""
Method that fetches every word pair in DB, and maps
every word to the sentence that contains the respective word.
"""
def build_word_sntc_mp():
   cnx = get_cnx()
   cursor = cnx.cursor()
   query_words = ("select * from word_mp;")
   cursor.execute(query_words)
   for (wid,en_wd,jp_wd) in cursor:
      #print wid, en_wd, jp_wd 
      #print "sentence having[",en_wd,"=",jp_wd,"]"
      #mapping_found = False
      en_list = sntc_having_word(en_wd)
      jp_list = sntc_having_word(jp_wd)
      for sid in (en_list | jp_list):
         inst_sntc_wd_pair(wid,sid)
         #mapping_found = True
      #if not mapping_found:
         #print "    nothing found"
   cnx.commit()
   cursor.close()
   cnx.close()
   return

def sntc_having_word(word):
   sntc_ids = set()
   cnx = get_cnx()
   cursor = cnx.cursor()
   query_sentences = ("select * from sentence_mp where " 
                 "english_sntc like \'%" + word + "%\'" +  
                 " or japanese_sntc like \'%" + word + "%\';")
   #search_param = (word,word)
   cursor.execute(query_sentences)
   for (sid,en_sntc,jp_sntc) in cursor:
      sntc_ids.add(sid)
      print "   ",sid, en_sntc, jp_sntc 
   cnx.commit()
   cursor.close()
   cnx.close()
   return sntc_ids 

def inst_sntc_wd_pair(wid,sid):
   cnx = get_cnx()
   cursor = cnx.cursor()
   add_mpg = ("INSERT INTO sentence_word_mp "
               "(sntc_id, word_id) "
               "VALUES (%s, %s)")
   data_mpg = (wid,sid)   
   cursor.execute(add_mpg,data_mpg)
   cnx.commit()
   cursor.close()
   cnx.close()
   return 

def word_having_chunk(chunk):
   word_ids = list()
   cnx = get_cnx()
   cursor = cnx.cursor()
   query = ("select * from word_mp where " 
                 "english_word like \'%" + chunk +"%\'" +  
                 " or japanese_word like \'%" + chunk +"%\';")
   #search_param = (word,word)
   cursor.execute(query)
   for (sid,en_word,jp_word) in cursor:
      word_ids.append(sid)
      #print "   ",sid, en_word, jp_word 
   cnx.commit()
   cursor.close()
   cnx.close()
   return word_ids

def get_word_pair_by_id(number):
   return_val = ("","")
   cnx = get_cnx()
   cursor = cnx.cursor()
   query=("select * from word_mp where word_id ="+str(number))
   #query_param = (number,)              
   cursor.execute(query)
   for (wid,en_word,jp_word) in cursor:
      return_val = (en_word,jp_word)
      #print "return_val = ",return_val
   cursor.close()
   cnx.close()
   return return_val
