#!/bin/python
import os


with open('xmen.txt','a') as xmen_file:
  xmen_file.writelines(["\n18\n","19\n"])


"""
xmen_file = open('xmen.txt','a')
# xmen_file.seek(-1,os.SEEK_END) # Used to append at the end of the file 

xmen_file.writelines(["\n15\n","16\n","17"])
#xmen_file_read = xmen_file.read()
"""

"""
for item in xmen_file_read:
  print "Hello Mr/Ms : %s " % item
"""
#print "Hello %s" % xmen_file.read()

#print "--------------------"
"""
for line in xmen_file:
  print "Hello %s" % line
"""
#print xmen_file.read()


xmen_file.close()
