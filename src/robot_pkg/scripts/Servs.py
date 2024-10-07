#!/usr/bin/python3 

import RPi.GPIO as GPIO
import board
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time
import rospy
from robot_pkg.msg import servodata, xy
from sensor_msgs.msg import Joy 

class startServs():
  angls = [0,90,90,90,90,90,90]    # Первый элемент - выбранный сервопривод. Остальные - углы сервоприводов.
  def __init__(self):
    startServs.i2c = board.I2C()  # uses board.SCL and board.SDA
    startServs.pca = PCA9685(startServs.i2c)
    startServs.pca.frequency = 100
    startServs.servo10 = servo.Servo(startServs.pca.channels[12], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    startServs.servo11 = servo.Servo(startServs.pca.channels[13], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    startServs.servo12 = servo.Servo(startServs.pca.channels[14], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    startServs.servo13 = servo.Servo(startServs.pca.channels[15], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    #startServs.servo14 = servo.Servo(startServs.pca.channels[16], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    #startServs.servo15 = servo.Servo(startServs.pca.channels[17], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    rospy.init_node('Servos')
    rospy.Subscriber("joy", Joy, self.callback_joy)
    
  @staticmethod
  def callback_joy(data) -> None:
    """
    Получение данных с джойстика, их обработка
    """
    #print(startServs.angls)
    if data.buttons[0] == 1:
      startServs.angls[0] = 1
    if data.buttons[1] == 1:
      startServs.angls[0] = 2
    if data.buttons[2] == 1:
      startServs.angls[0] = 3
    if data.buttons[3] == 1:
      startServs.angls[0] = 4

    if data.axes[0] < 0 and startServs.angls[startServs.angls[0]] > 20:
      startServs.angls[startServs.angls[0]] = startServs.angls[startServs.angls[0]] - 2
    if data.axes[0] > 0 and startServs.angls[startServs.angls[0]] < 160:
      startServs.angls[startServs.angls[0]] = startServs.angls[startServs.angls[0]] + 2
    
    startServs.servo10.angle = startServs.angls[1]
    startServs.servo11.angle = startServs.angls[2]
    startServs.servo12.angle = startServs.angls[3]
    startServs.servo13.angle = startServs.angls[4]
    startServs.servo14.angle = startServs.angls[5]
    startServs.servo15.angle = startServs.angls[6]

  @staticmethod
  def publis2topic() -> None:
    """
    Публикация в топик
    """
    startServs.srvData.servo0 = startServs.servo10.angle
    startServs.srvData.servo1 = startServs.servo11.angle
    startServs.srvData.servo2 = startServs.servo12.angle
    startServs.srvData.servo3 = startServs.servo13.angle
    startServs.srvData.servo4 = startServs.servo14.angle
    startServs.srvData.servo5 = startServs.servo15.angle
    startServs.pubServ.publish(startServs.srvData)

  @staticmethod
  def callback_mode(data) -> None:
    pass

def main():
  Ob = startServs()
  # Ob.move()
  rospy.spin()

if __name__=="__main__":
  main()
