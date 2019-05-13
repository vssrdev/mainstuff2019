#!/bin/python
import os

stage = (os.getenv("STAGY") or "development").upper()
output = "We are in %s environment" % stage

if stage.startswith("PROD"):
    output = "Danger ! " + output
print(output)

