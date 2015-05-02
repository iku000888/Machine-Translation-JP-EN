#!/bin/bash
#date '+%d/%m/%Y %H:%M:%S'> invocation_test.log
python ../main.py import-words wordmp.csv
python ../main.py import-sentences sntcmp.txt
echo "please refer DB dump or execute export test for sanity checking.."
