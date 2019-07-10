#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without

import keyboard  # using module keyboard
import rospy
from geometry_msgs.msg import Twist

def controlador_robo():

    rospy.init_node('controlador_robo')

    pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=10)
    vel_twist = Twist()
    rate = rospy.Rate(10)

    k_lin = 1
    k_ang = 0.7

    while True:
        vel_linear = 0
        vel_angular = 0
        key_pressed = False
        try:
            if keyboard.is_pressed('up'):
                key_pressed = True
                vel_linear += 1
            if keyboard.is_pressed('down'):
                key_pressed = True
                vel_linear -= 1
            if keyboard.is_pressed('left'):
                key_pressed = True
                vel_angular += 1
            if keyboard.is_pressed('right'):
                key_pressed = True
                vel_angular -= 1

            if key_pressed:
                vel_twist.linear.x = vel_linear * k_lin
                vel_twist.angular.z = vel_angular * k_ang
                pub.publish(vel_twist)
        except:
            break
        rate.sleep()


if __name__ == '__main__':
    try:
        controlador_robo()
    except rospy.ROSInterruptException:
        pass
