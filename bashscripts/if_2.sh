#!/bin/bash

read -p "Enter the number " NUM
echo 
echo "Enterd number is $NUM"

if [ $NUM -gt 100 ]
then
  echo "Inside If condition"
  echo " you have passed a large number"
  CurDir=$(pwd)
  echo "Current Working directory is $CurDir"
else
  echo "Enterer value is less than 100"
fi

date


