import mysql.connector
# -*- coding: utf-8 -*-

def insert_word_pair(en_word,jp_word):
   cnx = mysql.connector.connect(user='root', password='root',
                                 host='127.0.0.1',
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
