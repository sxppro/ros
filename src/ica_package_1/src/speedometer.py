#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)


def listener():
    rospy.init_node('carla_speedometer_listener')
    rospy.Subscriber("/carla/ego_vehicle/speedometer", Float32, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()


