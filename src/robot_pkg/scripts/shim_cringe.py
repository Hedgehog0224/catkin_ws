#!/usr/bin/python3 
import sys
from numpy import round
from math import cos, sin, pi

import RPi.GPIO as GPIO
import board
from adafruit_pca9685 import PCA9685

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from robot_pkg.msg import xy

# GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
if GPIO.getmode() == None:
    GPIO.setmode(GPIO.BOARD)  

from MatMotors import Route, Motor

class robotcl():
    I2Cpins = [0,1,2,5,3,4,6,8,7,11,9,10]
    mode = 0
    varStopAll = 0
    JoySpeed = [0.0, 0.0]
    JoyAngle = 0
    PredArrForMove = [0,0,0,0]
    
    A = Motor( 1,  0)
    B = Motor( 0,  1)
    C = Motor(-1,  0)
    D = Motor( 0, -1)
    
    abcd = Route(A, B, C, D)

    def __init__(self):
        rospy.init_node('MainNodeForRobot')
        rospy.Subscriber("scan", LaserScan, self.callback_scan)
        rospy.Subscriber("distance", Float32, self.callback_ultra_zd)
        rospy.Subscriber("Mode", xy, self.callback_mode)
        
    @staticmethod
    def callback_scan(data):
        if robotcl.varStopAll:
            robotcl.abcd.move(robotcl.abcd.set_speed(1, 1), [0, 0, 0, 0], robotcl.I2Cpins)
        elif robotcl.mode in [0,3]:
            robotcl.abcd.move([0, 0, 0, 0], [0, 0, 0, 0], robotcl.I2Cpins)
            rospy.loginfo_throttle(20, 'The mode in which the robot does not drive is selected: %s', robotcl.mode)
        elif robotcl.mode == 2:
            size = int(len(data.ranges))
        
            temp = min(data.ranges[int(size*0.1):int(size*0.9)])
            # print('NOTTTTTTT', min(data.ranges))
            if temp > 0.6:
                # print('stop')               
                rospy.loginfo_throttle(20, 'No obstacles detected, the robot is in rest mode: %s', round(temp, 2))
                robotcl.abcd.move([0, 0, 0, 0], [0, 0, 0, 0], robotcl.I2Cpins)
            else:
                # print('move')
                res = [i for i, j in enumerate(data.ranges) if j == temp]
                minNum = round(min(res)/size, 2)
                maxNum = round(max(res)/size, 2)
                if maxNum - minNum > size*0.5:
                    sr = minNum
                else: sr = (sum(res)/len(res))/size
        
                x = -sin(sr*2*pi)
                y = cos(sr*2*pi)
                # print('dir:', round(x,2), round(y,2))
                # pub_xy(x, y)
                
                ArrForMove = robotcl.abcd.set_speed(x, y)
                robotcl.abcd.move(ArrForMove, robotcl.PredArrForMove, robotcl.I2Cpins)
                #abcd.move([1,1,0,0], [0,0,0,0])
        
                robotcl.PredArrForMove = ArrForMove
        else:            
            JoyArr = robotcl.abcd.set_speed(robotcl.JoySpeed[0], robotcl.JoySpeed[1], turnOsSys=45, ModeOfAngles = 1, FuncOfAngel = [0, -robotcl.JoyAngle])
            robotcl.abcd.move(JoyArr, [0,0,0,0], robotcl.I2Cpins)
    
    @staticmethod
    def callback_ultra_zd(data):
        dataFloat = float(str(data)[6:-1])
        if dataFloat < 20.0:
            rospy.loginfo('Attention an obstacle has been detected (cm): %s', round(dataFloat,2))
            robotcl.varStopAll = True
        else:
            robotcl.varStopAll = False
    
    @staticmethod
    def callback_mode(data):
        robotcl.mode = data.mode
        robotcl.JoySpeed = [data.x, data.y]
        robotcl.JoyAngle = data.angle

cringebot = robotcl()
rospy.sleep(0.05)
rospy.spin()
