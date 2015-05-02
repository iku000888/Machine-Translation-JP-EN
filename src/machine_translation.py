import mysql.connector
#codecs module is necessary for writng utf-8 chars to a file.
import codecs
#Credential informations stored as env. vars.
import os
# -*- coding: utf-8 -*-

def get_cnx():
   cnx = mysql.connector.connect(user=os.environ["MYSQLID"],
                                 password=os.environ["MYSQLPW"],
                                 host=os.environ["MYSQLIP"],
                                 database='EN_JAP')
   return cnx

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

def export_word_pairs(outfile):
   #print outfile
   cnx = get_cnx()
   cursor = cnx.cursor()
   get_words = ("select * from word_mp;")
   cursor.execute(get_words)
   fo = codecs.open(outfile,"w","utf-8")
   for(english_word,japanese_word) in cursor:
      fo.write(u"{},{}".format(english_word,japanese_word)+u"\n");
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
   #map of translation directory to query used.
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


