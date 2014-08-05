#!/bin/bash -x
# Runs as 'root' in '/'

# See AWS EC2 instance /var/log/cloud-init[-output].log
echo "######################################################################"
echo `date` RUNNING USER DATA AS USER `whoami` IN DIR `pwd`

# Ubuntu 14.04 has python-2.7
apt-get update -y
apt-get install -y git python-virtualenv

# TODO: use a tag
# https avoids git: ssh asking to trust the key, hanging AWS
echo "## Clone the repo and change into it..."
cd ~ubuntu
git clone https://github.com/shentonfreude/autoscale-pyramid
chown -R ubuntu:ubuntu autoscale-pyramid 
cd autoscale-pyramid

# Build and run with scripts in the code repo for easy changes
# since AWS doesn't let us edit the User Data. Do this as ubuntu user.
echo "## Invoke the build and run scripts..."
su ubuntu -c "cd ~ubuntu/autoscale-pyramid && ./build.sh"
# Best to run server in background
su ubuntu -c "cd ~ubuntu/autoscale-pyramid && ./run.sh"

echo `date` FINISHED USER DATA AND BUILDING / RUNNING
echo "######################################################################"
