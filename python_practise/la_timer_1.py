#!/bin/python

import time

start_time = time.localtime()
print "Timer started at %s" %(time.strftime("%X",start_time))

raw_input("Press enter to continue....")

stop_time = time.localtime()
print "Timer stopped at %s" %(time.strftime("%X",stop_time))

# Difference between time 

diff = time.mktime(stop_time) - time.mktime(start_time)
print "Differnce of time in seconds is %s seconds:" % diff
