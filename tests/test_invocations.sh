#!/bin/bash
date '+%d/%m/%Y %H:%M:%S'> invocation_test.log
python ../main.py learn-word >> invocation_test.log
python ../main.py learn-sentence >> invocation_test.log
python ../main.py translate-word >> invocation_test.log
python ../main.py translate-sentence >> invocation_test.log
python ../main.py import-words >> invocation_test.log
python ../main.py 'export-words' >> invocation_test.log
python ../main.py import-sentences >> invocation_test.log
python ../main.py 'export-sentences' >> invocation_test.log
cat invocation_test.log
