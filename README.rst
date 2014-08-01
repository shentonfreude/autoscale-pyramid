================
 Autoscale Test
================

Simple app and userdata to learn autoscaling.

Deploy a Pyramid app which gets load, perhaps by intense
calculations. Since we're planning on an API server, let's do this via
URL request returning JSON response. A factorial calculator might
do. Return metadata bout the server so we can tell who's answering the
request. Example::

  GET /factorial/5

  {
    "metadata": {"server" : "10.1.2.3"},
    "query": "/factorial/5",
    "answer": 120
  }

User Data contains entire install instructions
==============================================

For the first attempt, use a bare Ubuntu AMI and have the User Data do
all the work. In a real enviornment, this work would delay bringing up
the service quickly. But it means the server instance can be generic,
and all code updates will be reflected at instance launch time.

We supply to the instances (via AS Launch Config) userdata which
updates the OS, installs the prerequisites (e.g., pyramid), and pulls
the code from GitHub and integrates it with Pyramid. There must be
some system startup script too.


User Data contains almost nothing
=================================

For the second attempt, create an Ubuntu instance and manually update
the OS, install the prerequisites and code on the system. Then burn an
AMI from this.  Configure the Launch Config to use this AMI.  Is there
anything the User Data needs to do?


How this hierarchy was created, run
==============================

Create virtualenv.
bin/pcreate -s starter autoscaletest
bin/python setup.py develop
[hack autoscaletest to contain your app]
bin/pserve autoscaletest/development.ini 

