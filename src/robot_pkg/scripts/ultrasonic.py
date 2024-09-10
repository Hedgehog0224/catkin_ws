#!/usr/bin/python3 
import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
import time


# class MakeUltrasonic():
def setUpPins(InPin, OutPin) -> None:
    ```
    Настройка пинов распы для корректной работы
    ```
    if GPIO.getmode() == None:
        GPIO.setmode(GPIO.BOARD)
    inputPin = InPin # connect to echo via 1K resistor
    outputPin = OutPin # connect to trig
    GPIO.setup(outputPin,GPIO.OUT)
    GPIO.setup(inputPin,GPIO.IN)
    GPIO.output(outputPin, False)
    time.sleep(0.1)
    GPIO.output(outputPin,True)
    time.sleep(0.00001)
    GPIO.output(outputPin,False)

def ultrasonic_detection(inputPin, outputPin, pub) -> None:
    ```
    Расчёт расстояния из времени, полученного от ультразвукового датчика
    ```
    setUpPins(inputPin, outputPin)
        
    while GPIO.input(inputPin) == 0:
        start = time.time()
    while GPIO.input(inputPin) == 1:
        stop = time.time()

    currentTime = stop - start
    distance = round(currentTime * 17150, 2)
    pub.publish(Float32(distance))

    # if chPrint: print("Distance is", distance, "cm")
    GPIO.cleanup()

def start() -> None:
    ```
    Публикация дистанции в топик distance
    ```
    # rospy.init_node('ultrasonic')
    pub = rospy.Publisher('distance', Float32, queue_size=10)
    while not rospy.is_shutdown():    
        distance = ultrasonic_detection(18, 16, pub)
        
if __name__=='__main__':
    rospy.init_node('UltrasonicNode')
    
    GPIO.setwarnings(False)
    if GPIO.getmode() == None:
        GPIO.setmode(GPIO.BOARD)

    start()
