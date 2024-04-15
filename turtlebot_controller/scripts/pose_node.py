#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    print("Pose information:\n  Position: x: {}, y: {}, z: {}\n  Orientation: w: {}, x: {}, y: {}, z: {}".format(
        msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z,
        msg.pose.pose.orientation.w, msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z
    ))

def main():
    rospy.init_node('pose_subscriber')
    rospy.Subscriber("/odom", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
