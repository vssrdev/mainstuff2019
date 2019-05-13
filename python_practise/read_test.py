#!/bin/python
import subprocess

#list1 = subprocess.check_output('cat /root/python_practise/test_file' , shell=True)

fo = open('test_file')
#print list1

line = fo.readlines()
for item in line:
  print "Hello : %s" % item

fo.close()
# print "Read line : %s" % line
