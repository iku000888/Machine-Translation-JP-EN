#!/bin/bash
#date '+%d/%m/%Y %H:%M:%S'> invocation_test.log

#must be in the test directory to run the unit test
#otherwise relative path will fail.
#ultimately, running this test without fail should assure the
#following:
#-MySql connection is working
#-Python is working
#-All modules on top of it are working.
#-text data can be processed.

#If necessary environment variables are not set,
#set them.
. ../src/set_environmet.sh

mysql --user=root --password=$MYSQLPW <../dbscripts/create_tables.txt
echo 'dropping and re-adding the tables...'
#from util module, which does not require DB connection
python random_splitter_test.py
python templetize_test.py

#from dao module, which does require DB connection.
python chunk_search_test.py
python translate_word_test.py
python build_map_test.py
