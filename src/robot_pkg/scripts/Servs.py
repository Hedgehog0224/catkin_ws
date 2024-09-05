#!/usr/bin/python3 

import RPi.GPIO as GPIO
import board
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time
import rospy
from robot_pkg.msg import servodata, xy

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
    self.servo12 = servo.Servo(self.pca.channels[12], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    self.servo13 = servo.Servo(self.pca.channels[13], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    self.servo14 = servo.Servo(self.pca.channels[14], actuation_range = 180, min_pulse = 750, max_pulse=2250)
    self.servo15 = servo.Servo(self.pca.channels[15], actuation_range = 180, min_pulse = 750, max_pulse=2250)

    rospy.init_node('Servos')
    # self.pubServ = rospy.Publisher('Servs', servodata, queue_size=10)
    # self.srvData = servodata()
    # rospy.Subscriber("Mode", xy, self.callback_mode)

  def move(self):
   # for i in range(180):
       #rospy.loginfo(i)
  self.servo15.angle = 40
   #     time.sleep(0.05)

   # for i in range(26):
   #     self.servo14.angle = 180-i*5
   #     time.sleep(0.1)
     
   # for i in range(36):
   #     self.servo15.angle = 180-i*5
   #     time.sleep(0.1)
     
   # for i in range(36):
   #     self.servo15.angle = i*5
   #     time.sleep(0.1)
     
   # for i in range(26):
   #     self.servo14.angle = 50+i*5
   #     time.sleep(0.1)
     
   # for i in range(180):
   #     #rospy.loginfo(i)
   #     self.servo12.angle = 180-i
   #     self.servo13.angle = 180-i
   #     self.servo14.angle = 180-i
   #     self.servo15.angle = 180-i
   #     time.sleep(0.05)

#    self.servo13.angle = 120
#    self.servo14.angle = 120
#    self.servo15.angle = 120

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
