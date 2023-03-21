#!/usr/bin/env python

import rospy
from ica_package_1.msg import CustomMsg


def send_message():
    pub = rospy.Publisher('/publisher', CustomMsg)
    rospy.init_node('sample_publisher')
    msg = CustomMsg()
    msg.vehicle_id = 'Soppro'
    msg.position_lat = float(233.120123123154)
    msg.position_long = float(123.258947023409)
    msg.isRoadLeader = True
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        send_message()
    except rospy.ROSInterruptException:
        pass
