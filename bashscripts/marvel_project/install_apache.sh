#!/bin/bash

#read -p "Enter web Directory: " Web_Dir
Web_Dir=2115_marvel
cat /etc/redhat-release
if [ $? -eq 0 ]
then
  echo "You are in redhat based system"
 
  echo "Updating yum repository.........."
  sudo yum update -y
 
  echo "Installing various packages......"
  sudo yum install wget unzip httpd -y

  echo "Starting httpd service..........."
  sudo systemctl start httpd
  
  echo "Enabling httpd......"
  sudo systemctl enable httpd

  echo "Downloading artifact from tooplate...."
  cd /tmp
  wget -O marvel.zip https://www.tooplate.com/download/2115_marvel
  unzip -o marvel.zip

  echo "Deploying artifacts......."
  sudo cp -r /tmp/$Web_Dir/* /var/www/html
  
  echo "Restarting httpd service"
  sudo systemctl restart httpd
else
  echo "You are in debain family"
  echo
  echo "Updating packages"
  sudo apt-get update -y
  echo "Installing various packages....."
  sudo apt-get install apache2 wget unzip -y
  
  echo "Starting Apache2 service..........."
  sudo systemctl start apache2

  echo "Enabling httpd......"
  sudo systemctl enable apache2
  
  
  echo "Downloading artifact from tooplate...."
  cd /tmp
  wget -O marvel.zip https://www.tooplate.com/download/2115_marvel
  unzip -o marvel.zip

  echo "Deploying artifacts......."
  sudo cp -r /tmp/$Web_Dir/* /var/www/html

  echo "Restarting httpd service"
  service apache2 restart
fi
