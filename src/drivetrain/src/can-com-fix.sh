#!/bin/bash

#LOGFILE=/var/log/can.log
LOGFILE=/home/sumitomo/Desktop/can.log

candump can0 > $LOGFILE &

