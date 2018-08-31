#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from geometry_msgs.msg import Point
from ar_track_alvar_msgs.msg import AlvarMarkers

def callback(msg):
    print 'yess'
    pub.publish(msg.markers[0].pose.pose.position)
    pub2.publish(msg.markers[0].id)


pub = rospy.Publisher('marker_xy', Point, queue_size=1)
pub2 = rospy.Publisher('marker_id', Int32, queue_size=1)
rospy.init_node('subpub', anonymous=True)
rate = rospy.Rate(10) # 10hz
rospy.Subscriber('ar_pose_marker', AlvarMarkers, callback)
while not rospy.is_shutdown():
    print 'h'
    
    rate.sleep()


