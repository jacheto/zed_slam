#! /usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import LaserScan
import datetime

def callback(s):
	dados = s.data
	text_file = open("/home/felipe/Documents/Output" + str(datetime.datetime.now().time()) + ".txt", "w")
	text_file.write(dados)
	text_file.close()
	print "----------------------------"

def node_aux():
	rospy.init_node('pointcloud_to_laserscan_caseiro_node')

	rospy.Subscriber('/zed/point_cloud/cloud_registered', PointCloud2, callback)

	rospy.spin()

if __name__ == '__main__':
    node_aux()