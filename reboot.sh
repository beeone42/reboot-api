#!/bin/sh
date >> reboot.log

# this script will be called only on service down notification
# add your reboot comman below

curl http://10.0.0.1/reboot.php &
