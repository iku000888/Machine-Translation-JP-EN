#!/bin/bash
#date '+%d/%m/%Y %H:%M:%S'> invocation_test.log
python ../src/main.py export-words export_words.csv
python ../src/main.py export-sentences export_sntc.txt
cat export_words.csv
