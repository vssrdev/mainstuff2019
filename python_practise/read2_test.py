#!/bin/python
import subprocess

fo = open('test_file','r+')
#print list1
fo.writelines(["\nVarre\n","Singupuram"])

line = fo.readlines()
for item in line:
  print "Hello : %s" % item.strip()
#fo.write("New Line")

fo.close()
# print "Read line : %s" % line
