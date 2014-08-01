#!/bin/bash
# Ubuntu 14.04 has python-2.7
apt-get update -y
apt-get install -y git python-virtualenv

# become mortal, change to ~ubuntu
su - ubuntu

# Should do a tag
# https avoids git: ssh asking to trust the key, hanging AWS
git clone https://github.com/shentonfreude/autoscale-pyramid
cd autoscale-pyramid ~

./build.sh
# Should run in background or AWS init might never complete?
./run.sh


