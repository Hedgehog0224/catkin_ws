import rospy
from sensor_msgs.msg import Joy

def callback_joy(data) -> None:
  ```
  Вывод данных с джойстика в терминал для тестирования кнопок (вывода данных)
  ```
  print(data.axes)
  print(data.buttons)


rospy.init_node('Get_Data_From_Joy')
rospy.Subscriber("scan", Joy, callback_joy)
rospy.sleep(0.05)
rospy.spin()
