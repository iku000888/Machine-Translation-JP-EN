import os
import sys

print "MYSQL ip address, please"
os.environ["MYSQLIP"] = sys.stdin.readline()
print "id please"
os.environ["MYSQLID"] = sys.stdin.readline()
print "password, please"
os.environ["MYSQLPW"] = sys.stdin.readline()
