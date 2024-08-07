#!/usr/bin/python3 
import sys
from numpy import round, array
from math import cos, sin, pi
from time import sleep, time

import RPi.GPIO as GPIO
import board
from adafruit_pca9685 import PCA9685

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan
from robot_pkg.msg import xy

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
            stTime = time()
            new_data = array(data.ranges[0:int(len(data.ranges)*0.4)] + data.ranges[int(len(data.ranges)*0.6):int(len(data.ranges))])
            size_nd = len(new_data)
            temp = min(new_data)
            # stop               
            if temp > 0.6:
                rospy.loginfo_throttle(20, 'No obstacles detected, the robot is in rest mode: %s', round(temp, 2))
                robotcl.abcd.move([0, 0, 0, 0], [0, 0, 0, 0], robotcl.I2Cpins)
            # move
            else:
                minArr = [i for i, j in enumerate(new_data) if j == temp]
                border = [min(minArr), max(minArr)]
                if border[1] - border[0] > size_nd/2:
                    sr = abs(((border[0] + border[1])/2)-size_nd/2)
                else:
                    sr = (border[0] + border[1])/2
                x = cos((sr/size_nd)*2*pi)
                y = sin((sr/size_nd)*2*pi)
                ArrForMove = robotcl.abcd.set_speed(x, y)
                robotcl.abcd.move(ArrForMove, robotcl.PredArrForMove, robotcl.I2Cpins)
                robotcl.PredArrForMove = ArrForMove
                workTime = time() - stTime
                rospy.loginfo("Time work: %s", workTime)
        else:            
            JoyArr = robotcl.abcd.set_speed(robotcl.JoySpeed[0], robotcl.JoySpeed[1], turnOsSys=45, ModeOfAngles = 1, FuncOfAngel = [0, -robotcl.JoyAngle])
            if ((abs(JoyArr[0])<0.05) and (abs(JoyArr[1])<0.05) and (abs(JoyArr[2])<0.05) and (abs(JoyArr[3])<0.05)):
                rospy.loginfo("Stoping...")
                robotcl.abcd.move([-robotcl.PredArrForMove[0]*2, -robotcl.PredArrForMove[1]*2, -robotcl.PredArrForMove[2]*2, -robotcl.PredArrForMove[3]*2], [0,0,0,0], robotcl.I2Cpins)
                sleep(0.05)
            robotcl.abcd.move(JoyArr, [0,0,0,0], robotcl.I2Cpins)
            robotcl.PredArrForMove = JoyArr
    
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