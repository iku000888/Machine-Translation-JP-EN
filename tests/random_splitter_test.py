import sys
sys.path.append('../src/')
import mac_tran_utils as util
input_str="This is a string to be split, please take a look at what happens"
print util.random_split(input_str)
print util.random_split(input_str[::-1])
