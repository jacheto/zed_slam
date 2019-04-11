#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import rospy
from std_msgs.msg import String
from zed_slam.msg import Distancias
from zed_slam.msg import MovimentoBase

def callback(sd):
    
    motorE = 0
    motorD = 0
    if sd.SensorC < 0.5:
        motorE = -150
        motorD = -150
    else:
        motorE = 150
        motorD = 150
    
    mb = MovimentoBase()
    mb.VelMotorE = motorE
    mb.VelMotorD = motorD
    
    pub = rospy.Publisher('MovimentoBase', MovimentoBase, queue_size=10)
    pub.publish(mb)
    print("Motores: " + str(motorE))
    
def interface_arduino():
    
    rospy.init_node('interface_arduino')
    
    rospy.Subscriber('SensoresDistancia', Distancias, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        interface_arduino()
    except rospy.ROSInterruptException:
        pass
