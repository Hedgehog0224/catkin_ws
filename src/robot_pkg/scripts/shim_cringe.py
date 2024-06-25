#!/usr/bin/python3 
import threading
import sys
import time
from numpy import arange, round
from math import cos, sin, pi

import RPi.GPIO as GPIO
import board
from adafruit_pca9685 import PCA9685
from evdev import InputDevice, categorize, ecodes, KeyEvent

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan

# GPIO.setmode(GPIO.BOARD)
start_time = time.time()
GPIO.setwarnings(False)
if GPIO.getmode() == None:
    GPIO.setmode(GPIO.BOARD)  

Speed = [0.0, 0.0]
PredArrForMove = [0,0,0,0]

from MatMotors import Route, Motor

A = Motor( 1,  0)
B = Motor( 0,  1)
C = Motor(-1,  0)
D = Motor( 0, -1)

abcd = Route(A, B, C, D)
cod2 = 0
cod5 = 0

a = 0
b = 0
c = 0
d = 0

varStopAll = False

def callback_scan(data):
    global varStopAll
    global PredArrForMove
    
    if varStopAll:
        print('=== Obstacle ===')
    else:
        size = int(len(data.ranges))
    
        temp = min(data.ranges[int(size*0.1):int(size*0.9)])
        # print('NOTTTTTTT', min(data.ranges))
        if temp > 0.6:
            print('stop')
            abcd.move([0, 0, 0, 0], [0, 0, 0, 0])
        else:
            print('move')
            res = [i for i, j in enumerate(data.ranges) if j == temp]
            minNum = round(min(res)/size, 2)
            maxNum = round(max(res)/size, 2)
            if maxNum - minNum > size*0.5:
                sr = minNum
            else: sr = (sum(res)/len(res))/size
    
            x = -sin(sr*2*pi)
            y = cos(sr*2*pi)
            # print('dir:', round(x,2), round(y,2))
            pub_xy(x, y)
            
            ArrForMove = abcd.set_speed(x, y)
            abcd.move(ArrForMove, PredArrForMove)
            #abcd.move([1,1,0,0], [0,0,0,0])
    
            if time.time() - start_time > 360:
                abcd.move([0, 0, 0, 0], [0, 0, 0, 0])
                sys.exit()
            PredArrForMove = ArrForMove

def callback_ultra_zd(data):
    dataFloat = float(str(data)[6:-1])
    if dataFloat < 20.0:
        print('Attention an obstacle has been detected')
        abcd.move([0, 0, 0, 0], [0, 0, 0, 0])
        varStopAll = True
    else:
        varStopAll = False
def pub_xy(x, y):
    global pubx
    global puby
    pubx.publish(x)
    puby.publish(y)

rospy.init_node('MainNodeForRobot')
pubx = rospy.Publisher('Xspeed', Float32, queue_size=10)
puby = rospy.Publisher('Yspeed', Float32, queue_size=10)

rospy.Subscriber("scan", LaserScan, callback_scan)
rospy.Subscriber("distance", Float32, callback_ultra_zd)

rospy.sleep(0.05)
rospy.spin()
