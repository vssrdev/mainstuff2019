#!/usr/bin/python

import os

user_list = ["siva","indu","maha","dev"]

print "Adding users to system"

print "########################"

#Loop to add user from user list
for user in user_list:
  exitcode = os.system(("id %s") %user)
  if exitcode != 0 :
    print "User %s doesnot exists, Adding %s user" %(user,user)
    print "##########################################"
    os.system(("useradd %s") %user)
  else:
    print "User %s exists" %user

