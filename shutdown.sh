#!/bin/bash

PIN=388

echo $PIN > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio$PIN/direction

while true
do
  file="/sys/class/gpio/gpio$PIN/value"
  STATUS=$(cat "$file")
  echo $STATUS  
  if [ $STATUS -eq 1 ]
  then
    $(ros-net-init-stop)
    sleep 5
    $(shutdown now)
  fi
  sleep .2

done
