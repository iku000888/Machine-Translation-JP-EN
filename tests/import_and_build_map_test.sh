#!/bin/bash
#date '+%d/%m/%Y %H:%M:%S'> invocation_test.log

#clear DB before inserting
../dbscripts/connect_db.sh ../dbscripts/create_tables.txt
python ../src/main.py import-words wordmp.csv
python ../src/main.py import-sentences sntcmp.txt
python ../src/main.py build-sentence-word-mp 
echo "please refer DB dump or execute export test for sanity checking.."
