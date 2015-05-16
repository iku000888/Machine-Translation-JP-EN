#!/bin/bash
#date '+%d/%m/%Y %H:%M:%S'> invocation_test.log
python ../main.py export-words export_words.csv
python ../main.py export-sentences export_sntc.txt
cat export_test.csv
