#!/usr/bin/env python2.7
import rospy
import subprocess
import time
import os
from canopen_chain_node.srv import GetObject
from std_srvs.srv import Trigger

PIN= "398" #GPIO
node= 'motorRight'

REBOOT= ["shutdown", "-h", "now"]

#Function to verify the status from the driver, if it is "fault" it will restart all the system


def initSmartrisGet(node,obj):
        #Code that generates the sequence to get the Smartris to run state
        #rosservice that changes objects form the eds
        get_object = rospy.ServiceProxy("driver/get_object", GetObject, persistent=True) #  , persis$
        try:

                # call the rosservice with your node name, object and the value you want
                # last value is a boolean for the cached part of the setObject msg
                service_call = get_object(node,obj, True)
               # print("Servie response is:" , service_call)
                return service_call
        except rospy.ServiceException as e:
                # catch any errors
                print("Service call failed: %s"%e)

time.sleep(10)

print("------------VERIFYING DRIVER STATUS-----------------")
get_lecture= initSmartrisGet(node,'0x6041')
get_value= get_lecture.value
print("get_value: ", get_value)
if ((get_value == '37023') or (get_value == "37535")): # or (get_value == "4663")):
    print("Fault code detected. Restarting...")

    f = open("/sys/class/gpio/gpio"+PIN+"/value" , "a")
    f.write("1") #GPIO PIN ON
    f.close()

    os.system("ros-net-init-stop")

  #  time.sleep(1)

#    f = open("/sys/class/gpio/gpio"+PIN+"/value" , "a")
#    f.write("0") #GPIO PIN ON
  #  f.close()

    
#    os.system("sudo shutdown -h now")
#    subprocess.call(REBOOT)

