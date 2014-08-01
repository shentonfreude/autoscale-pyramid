#!/bin/bash
echo `date` RUNNING USER DATA

# Ubuntu 14.04 has python-2.7
apt-get update -y
apt-get install -y git python-virtualenv

# become mortal, change to ~ubuntu
su - ubuntu

# TODO: use a tag
# https avoids git: ssh asking to trust the key, hanging AWS
git clone https://github.com/shentonfreude/autoscale-pyramid
cd autoscale-pyramid ~

# Build and run with scripts in the code repo for easy changes
# since AWS doesn't let us edit the User Data.
./build.sh
# Should run in background or AWS init might never complete?
./run.sh

echo `date` FINISHED USER DATA AND BUILDING / RUNNING
