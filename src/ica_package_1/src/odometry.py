#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' %s', data)


def listener():
    rospy.init_node('carla_odometry_listener')
    rospy.Subscriber("/carla/ego_vehicle/odometry", Odometry, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()


