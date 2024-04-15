#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('publisher_node_2')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    msg = Twist()
    start_time = rospy.get_time()
    msg.linear.x = 1.0

    rospy.loginfo('Node started')
    
    while not rospy.is_shutdown():
        #msg.angular.z = 1.0
        pub.publish(msg)
        current_time = rospy.get_time()
        traveled_time = current_time - start_time
        covered_distance = msg.linear.x * traveled_time

        if covered_distance <=2.0:
            pub.publish(msg)
        else:
            break
        rate.sleep()