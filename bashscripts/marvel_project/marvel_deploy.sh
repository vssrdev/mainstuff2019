#!/bin/bash

#Push marvel website to all the machines

for IP in `cat marvel_hostsIP`
do
  echo "Pushing script to $IP"
  scp install_apache.sh devops@$IP:/tmp
done

for IP in `cat marvel_hostsIP`
do
  echo "Installing script on $IP machine"
  ssh devops@$IP /tmp/install_apache.sh
done
