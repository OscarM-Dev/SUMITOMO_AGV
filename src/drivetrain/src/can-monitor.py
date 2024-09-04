#!/usr/bin/env python3

import subprocess
import time

LAST_MSG_CMD = ["tail", "-n", "1", "/home/sumitomo/Desktop/can.log"]

CAN_RESET = ["python2.7", "/home/sumitomo/Documents/SumiyomoAGV/sumitomo_ws/src/drivetrain/src/SmartrisDriverInit.py"]

DRIVER_STATUS = ["python2.7", "/home/sumitomo/Documents/SumiyomoAGV/sumitomo_ws/src/drivetrain/src/get-fun.py"]

subprocess.run(CAN_RESET) #First DriverInit

##Can bus verification###
flag= False
while flag:
    time.sleep(.2)
    last_msg_output= subprocess.check_output(LAST_MSG_CMD)

    last_msg = last_msg_output.decode().strip()
    print (last_msg)
    if 'can0  701   [1]  7F' in last_msg or last_msg == '':
        print('Fault code in can communication. Reconnecting...\n\n\n')
        subprocess.run(CAN_RESET)
#        subprocess.run(CAN_RESET_UP)
    else:
        flag= True
    #time.sleep(3)

###  status driver verification ###

subprocess.run(DRIVER_STATUS)

