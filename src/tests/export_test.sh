#!/bin/bash
#date '+%d/%m/%Y %H:%M:%S'> invocation_test.log
python ../main.py export-words export_test.csv
cat export_test.csv
