#!/usr/bin/python
import os
import subprocess


if os.path.exists("/etc/redhat-release"):
    print("This is redhat machine")
else:
    print "This is ubuntu mahcine"


output_text = subprocess.check_output("cat /etc/redhat-release",shell=True)
if "CentOS" in output_text:
    print("This is redhat family")
else:
    print("This is Ubuntu")

