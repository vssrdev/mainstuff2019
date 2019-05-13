#!/usr/bin/python
import os

user_list = ["siva","indu","maha","varre"]

for user in user_list:
    exitcode = os.system("id %s" %user)
    if exitcode == 0:
        print "User %s Exists....." %user
    else:
        print "User %s doesn't exist, Adding %s:" %(user,user)
        os.system("useradd %s" %user)
        print "User %s added succesfully" %user

# condition to check if group exists, if not add group
exitcode_group = os.system("grep science /etc/group")

if exitcode_group != 0:
    print "Group Science doesn't exists, Adding Group"
    os.system("groupadd science")
else:
    print "Group science already exists, hence skipping ..."

# Adding existing users to Science group
for user in user_list:
    print "Adding %s user to science group" %user
    os.system(("usermod -G science %s") %user)
