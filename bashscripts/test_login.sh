#!/bin/bash
for IP in `cat marvel_hostsIP`
do
  ssh devops@$IP uptime
done
