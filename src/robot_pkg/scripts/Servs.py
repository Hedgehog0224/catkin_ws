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
  angls = [0,90,90,90,90,90,90]
  def __init__(self):
    self.i2c = board.I2C()  # uses board.SCL and board.SDA
    self.pca = PCA9685(self.i2c)
    self.pca.frequency = 100
    startServs.servo10 = servo.Servo(self.pca.channels[10], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    startServs.servo11 = servo.Servo(self.pca.channels[11], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    startServs.servo12 = servo.Servo(self.pca.channels[12], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    startServs.servo13 = servo.Servo(self.pca.channels[13], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    startServs.servo14 = servo.Servo(self.pca.channels[14], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    startServs.servo15 = servo.Servo(self.pca.channels[15], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    
    rospy.init_node('Servos')

    rospy.Subscriber("joy", Joy, self.callback_joy)
  @staticmethod
  def callback_joy(data):
    print(data)
    #huj
    if data.buttons[1] == 1:
      startServs.angls[0] = 1
    if data.buttons[2] == 1:
      startServs.angls[0] = 2
    if data.buttons[3] == 1:
      startServs.angls[0] = 3
    if data.buttons[4] == 1:
      startServs.angls[0] = 4
    if data.buttons[5] == 1:
      startServs.angls[0] = 5
    if data.buttons[6] == 1:
      startServs.angls[0] = 6

    if data.axes[0] < 0 and startServs.angls[startServs.angls[0]] > 20:
      startServs.angls[startServs.angls[0]] = startServs.angls[startServs.angls[0]] - 10
    if data.axes[0] > 0 and startServs.angls[startServs.angls[0]] < 160:
      startServs.angls[startServs.angls[0]] = startServs.angls[startServs.angls[0]] + 10
    
    startServs.servo10.angle = startServs.angls[1]
    startServs.servo11.angle = startServs.angls[2]
    startServs.servo12.angle = startServs.angls[3]
    startServs.servo13.angle = startServs.angls[4]
    startServs.servo14.angle = startServs.angls[5]
    startServs.servo15.angle = startServs.angls[6]
  
  def publis2topic(self):
    self.srvData.servo0 = self.servo10.angle
    self.srvData.servo1 = self.servo11.angle
    self.srvData.servo2 = self.servo12.angle
    self.srvData.servo3 = self.servo13.angle
    self.srvData.servo4 = self.servo14.angle
    self.srvData.servo5 = self.servo15.angle
    self.pubServ.publish(self.srvData)

  @staticmethod
  def callback_mode(data):
    pass
Ob = startServs()
# Ob.move()
rospy.spin()
