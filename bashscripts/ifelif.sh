#!/bin/bash
value=$(ip addr show | grep -v LOOPBACK | grep -ic mtu)

if [ $value -eq 1 ]
then
  echo "One active n/w interface found"
elif [ $value -gt 1 ]
then
  echo "More than 1 active interfaces found"
else
  echo "No interace found "
fi

echo "--------------------------------------------------------"


if [ -f /etc/redhat-release ]
then
  echo "File exists"
fi

