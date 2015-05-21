import random
def random_split(str_to_split):
   splitted_list = list()
   while len(str_to_split)>=1:
      #print "loop start"
      len_chunk=1+int(round(random.random()*len(str_to_split)))
      #print "lenchunk=",len_chunk
      chunk=str_to_split[0:len_chunk]
      #print "chunk=",chunk
      splitted_list.append(chunk)
      #print "list=",splitted_list
      str_to_split=str_to_split[len_chunk:len(str_to_split)]
      #print str_to_split
      #print "end of loop"
   print splitted_list
   return

def balanced_split(str_to_split):
   print str_to_split
   return

random_split("yolo, this is a very long string. I am on a train")
