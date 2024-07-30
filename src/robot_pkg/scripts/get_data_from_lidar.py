import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

def callback(data):
    size = int(len(data.ranges))

    temp = min(data.ranges)
    res = [i for i, j in enumerate(data.ranges) if j == temp]

    minNum = round(min(res)/size, 2)
    maxNum = round(max(res)/size, 2)
    sr = round((sum(res)/len(res))/size, 2)
    pub.publish(str([sr, minNum, maxNum]))

rospy.init_node('Get_Data_From_Lidar')
rospy.Subscriber("scan", LaserScan, callback)
pub = rospy.Publisher('DataFromLidar', String, queue_size=10)

rospy.sleep(0.05)
rospy.spin()

