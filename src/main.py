import sys

#print sys.argv[0]

#print sys.argv[1]

if "learn-word"==sys.argv[1]:
   print "stub: learn-word(a,b)"
elif "learn-sentence"==sys.argv[1]:
   print "stub: learn-sentence(a,b)"
elif "translate-word"==sys.argv[1]:
   print "stub: translate-word"
elif "translate-sentence"==sys.argv[1]:
   print "stub: translate-sentence"
elif "import-words"==sys.argv[1]:
   print "stub: import-words(a,b)"
elif "import-sentences"==sys.argv[1]:
   print "stub: import-sentence(a,b)"
elif "export-words"==sys.argv[1]:
   print "stub: export-words(a,b)"
elif "export-sentences"==sys.argv[1]:
   print "stub: export-sentences(a,b)"
else : 
   print "error: no such command"
