#!/usr/bin/env python
import roslib
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from geometry_msgs.msg import Point
from ar_track_alvar_msgs.msg import AlvarMarkers
import math
import tf

id = Int32()

listener = tf.TransformListener()

def callback(msg):
    print 'Publishing'
    #ADD if case to avoid array access index error
    pub.publish(msg.markers[0].pose.pose.position)
    id = msg.markers[0].id
    pub2.publish(id)
    try:
        (trans,rot) = listener.lookupTransform('/odom', '/ar_marker_' + str(id), rospy.Time(0))
        print trans
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        print 'error'

pub = rospy.Publisher('marker_xy', Point, queue_size=1)
pub2 = rospy.Publisher('marker_id', Int32, queue_size=1)
rospy.init_node('subpub', anonymous=True)
rate = rospy.Rate(10) # 10hz
rospy.Subscriber('ar_pose_marker', AlvarMarkers, callback)
while not rospy.is_shutdown():
    print 'ARtagpython is Running'
    
    
    rate.sleep()


