#!/bin/bash
# Ubuntu 14.04 has python-2.7
OUT=/home/ubuntu/USERDATA.out
apt-get update -y
apt-get install -y git python-virtualenv

echo "apt-get done" >> $OUT

# become mortal, change to ~ubuntu
su - ubuntu

echo "cloning..." >> ~/ubuntu/USERDATA.txt
# https avoids git: ssh asking to trust the key; Should do a tag
git clone https://github.com/shentonfreude/autoscale-pyramid

echo "building..." >> ~/ubuntu/USERDATA.txt
cd autoscale-pyramid ~
virtualenv .
bin/pip install pyramid==1.5.1

echo "run in background..." >> ~/ubuntu/USERDATA.txt
bin/python app.py &

