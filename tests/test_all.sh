#!/bin/bash
#date '+%d/%m/%Y %H:%M:%S'> invocation_test.log

#must be in the test directory to run the unit test
#otherwise relative path will fail.

#If necessary environment variables are not set,
#set them.
. ../src/set_environmet.sh

mysql --user=root --password=$MYSQLPW <../dbscripts/create_tables.txt
echo 'dropping and re-adding the tables...'
python random_splitter_test.py
python chunk_search_test.py
python translate_word_test.py
