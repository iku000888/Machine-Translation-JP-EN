#Simple demonstration of inserting a utf-8 string into
#mysql table
import mysql.connector
# -*- coding: utf-8 -*-

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='EN_JAP')
cursor = cnx.cursor()

add_word = ("INSERT INTO word_mp "
               "(english_word, japanese_word) "
               "VALUES (%s, %s)")
data_word = ('flower','花')

cursor.execute(add_word,data_word)
cnx.commit()
cursor.close()
cnx.close()
