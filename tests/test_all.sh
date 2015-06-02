#!/bin/bash
#date '+%d/%m/%Y %H:%M:%S'> invocation_test.log

#must be in the test directory to run the unit test
#otherwise relative path will fail.
. ../src/set_environmet.sh
mysql --user=root --password=$MYSQLPW <../dbscripts/create_tables.txt
echo 'dropping and re-adding the tables...'
set LOG_DEST 'test_artifacts/PyUnit.log'
python random_splitter_test.py > LOG_DEST
python chunk_search_test.py >> LOG_DEST
