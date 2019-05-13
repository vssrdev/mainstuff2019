#!/usr/bin/python
import os 
exit_code = os.system("cat /etc/redhat-release")
if exit_code == 0:
    print "Redhat"
else:
    print"Ubuntu"
