#!/bin/bash
# Ubuntu 14.04 has python-2.7
apt-get update -y
apt-get install -y python-virtualenv
virtualenv .
bin/pip install pyramid==1.5.1
# get the code

