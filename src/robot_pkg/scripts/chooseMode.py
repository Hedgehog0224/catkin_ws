#!/usr/bin/python3
import rospy
from robot_pkg.msg import xy
from sensor_msgs.msg import Joy

class chooseModeClass():
  pubMode = rospy.Publisher('Mode', xy, queue_size=10)
  rospy.init_node('chooseMode')
  msg = xy()
  msg.x = 0
  msg.y = 0

  def __init__(self):
    rospy.Subscriber("joy", Joy, self.callback_joy)
    
  @staticmethod
  def callback_joy(data):
    #print(data.axes)
    #print(data.buttons)
    if data.axes[2] + data.axes[5] < -1.9:
        chooseModeClass.msg.mode = 3
    elif data.axes[2] < 0:
        chooseModeClass.msg.mode = 1
    elif data.axes[5] < 0:
        chooseModeClass.msg.mode = 2
    else: chooseModeClass.msg.mode = 0
    chooseModeClass.msg.x = data.axes[4]
    chooseModeClass.msg.y = -data.axes[3]
    chooseModeClass.msg.angle = data.axes[0]
    chooseModeClass.pubMode.publish(chooseModeClass.msg)

robot = chooseModeClass()
rospy.sleep(0.05)
rospy.spin()
