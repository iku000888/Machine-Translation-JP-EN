#load all tests and run them all.
#for the time being, need to invoke the set_environment script
#to set up data base informations.
import unittest
import os
import sys

print "MYSQL ip address, please"
os.environ["MYSQLIP"] = sys.stdin.readline()
print "id please"
os.environ["MYSQLID"] = sys.stdin.readline()
print "password, please"
os.environ["MYSQLPW"] = sys.stdin.readline()

loader = unittest.TestLoader()
mods = loader.discover('.',pattern='*test*.py',top_level_dir=None)
suite = unittest.TestSuite(mods)
print suite 
runner = unittest.TextTestRunner()
runner.run(suite)
