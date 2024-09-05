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
  def __init__(self):
#    WORK_TIME = 10
#    DUTY_CYCLE = 50
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(GPIO_PWM_0, GPIO.OUT)
#    GPIO.setup(GPIO_PWM_1, GPIO.OUT)
#    servo0 = GPIO.PWM(12, 100) # pin, FREQUENCY
#    servo1 = GPIO.PWM(13, 100) # pin, FREQUENCY
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
    # self.pubServ = rospy.Publisher('Servs', servodata, queue_size=10)
    # self.srvData = servodata()
    # rospy.Subscriber("Mode", xy, self.callback_mode)

    rospy.Subscriber("joy", Joy, self.callback_joy)
  @staticmethod
  def callback_joy(data):
    print(data)
    Y=[1,0]
    B=[1,0]
    A=[1,0]
    X=[1,0]
    angls = [90,90,90,90,90,90]
    if data.buttons[4] == 1:
      ToggleY = Y[ToggleY]
      ToggleB = 0
      ToggleA = 0
      ToggleX = 0

    if data.buttons[5] == 1:
      ToggleB = B[ToggleB]
      ToggleA = 0
      ToggleX = 0
      ToggleY = 0

    if data.buttons[6] == 1:
      ToggleA = A[ToggleA]
      ToggleB = 0
      ToggleX = 0
      ToggleY = 0
#huj
    if data.buttons[7] == 1:
      ToggleX = X[ToggleX]
      ToggleB = 0
      ToggleA = 0
      ToggleY = 0

    if data.axes[0] > 0:
      s

    if ToggleA:
      startServs.servo10 = data.axes[0]
    if ToggleA:
      startServs.servo10 = data.axes[0]
    if ToggleA:
      startServs.servo10 = data.axes[0]
    if ToggleA:
      startServs.servo10 = data.axes[0]

  def publis2topic(self):
    self.srvData.servo0 = 0
    self.srvData.servo1 = self.servo12.angle
    self.srvData.servo2 = 2
    self.srvData.servo3 = 3
    self.srvData.servo4 = 4
    self.srvData.servo5 = 5
    self.pubServ.publish(self.srvData)

  @staticmethod
  def callback_mode(data):
    pass
Ob = startServs()
Ob.move()
rospy.spin()
