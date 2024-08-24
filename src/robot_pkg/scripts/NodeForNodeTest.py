#!/usr/bin/python3

import rospy
from std_msgs.msg import Int8

class TestNode():
    def __init__(self):
        rospy.init_node('TestNode')
        self.TestPub = rospy.Publisher('TestTopic', Int8, queue_size=20)

    def pub(self):
        for i in range(127):
            self.TestPub.publish(Int8(i))
            rospy.sleep(0.05)
        rospy.loginfo("Done!")

if __name__=='__main__':
    TestObj = TestNode()
    TestObj.pub()
    # rospy.spin()