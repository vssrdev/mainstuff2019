#!/bin/python
import os

stagg = (os.getenv("STAGY") or "development").upper()
output = "We are in %s environemnt" % stagg


if stagg.startswith("PROD"):
  output = "Danger" + output


print output
  
