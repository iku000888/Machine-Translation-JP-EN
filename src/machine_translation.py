import mysql.connector
#codecs module is necessary for writng utf-8 chars to a file.
import codecs
#Credential informations stored as env. vars.
import os
# -*- coding: utf-8 -*-

def insert_word_pair(en_word,jp_word):
   cnx = mysql.connector.connect(user=os.environ["MYSQLID"],
                                 password=os.environ["MYSQLPW"],
                                 host=os.environ["MYSQLIP"],
                                 database='EN_JAP')
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
   cnx = mysql.connector.connect(user=os.environ["MYSQLID"],
                                 password=os.environ["MYSQLPW"],
                                 host=os.environ["MYSQLIP"],
                                 database='EN_JAP')
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

