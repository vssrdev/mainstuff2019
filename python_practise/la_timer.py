"""
# Importing complete TIME package
import time

start_time = time.localtime()

print("Timer start at %s" % time.strftime("%X",start_time))

print(start_time)

time.mktime()

"""

# Importing only what is required from TIME package

from time import localtime,mktime,strftime

start_time = localtime()
print("Timer started at %s" % strftime("%X",start_time))

raw_input("Press enter to continue....")

stop_time = localtime()
print("Timer stopped at %s" % strftime("%X",stop_time))

difference = mktime(stop_time) - mktime(start_time)

print("Total time is %s Seconds" % difference)

