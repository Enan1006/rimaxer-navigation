#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('navigate_rimaxer')
    rospy.loginfo('Running')
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z=1.0
        pub.publish(msg)
        rate.sleep() 