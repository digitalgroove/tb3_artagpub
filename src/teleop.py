#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

def callback(data):
    twist = Twist()
    twist.linear.x = 4*data.axes[1]
    twist.angular.z = 4*data.axes[0]
    but1 = data.buttons[0] 
    if not but1:
        twist.linear.x = 0
        twist.angular.z = 0
    pub.publish(twist)

# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("/joy", Joy, callback)
    # starts the node
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Joy2Turtle')
    start()
