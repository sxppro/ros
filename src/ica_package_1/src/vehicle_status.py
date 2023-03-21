#!/usr/bin/env python

import rospy
import carla_msgs
from carla_msgs.msg import CarlaEgoVehicleStatus


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' %s', data)


def listener():
    rospy.init_node('carla_vehicle_status_listener')
    rospy.Subscriber("/carla/ego_vehicle/vehicle_status", CarlaEgoVehicleStatus, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()


