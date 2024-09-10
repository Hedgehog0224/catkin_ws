from numpy import arange, deg2rad, round, array
from math import sin, cos, atan
from random import random
from typing import Tuple

import RPi.GPIO as GPIO
import board
from adafruit_pca9685 import PCA9685

from rospy import logerr, loginfo, logwarn


class Motor():
    def __init__(self, x_multi, y_multi):
        GPIO.setwarnings(False)
        if GPIO.getmode() == None:
            GPIO.setmode(GPIO.BOARD)  
        
        self.L = 19.09            # Расстояние от центра до колеса
        self.speed = 0            # Скорость вращения колеса
        self.speed_shim = 0       # Скорость вращения колеса (пересчёт для контроллера)
        self.x_multi = x_multi    # Множитель по x
        self.y_multi = y_multi    # Множитель по y

    def _single_front_potate(self, V, fid) -> None:
        ```
        Вычисление скорости колеса (экземпляра) из скоростей (x, y)
        ```
        self.speed =  self.x_multi*V[0] + self.y_multi*V[1] + fid

    def set_speed_shim(self, newSpeed) -> None:
        ```
        Установка скорости вращения колеса для ШИМ-а
        ```
        self.speed_shim = newSpeed


class Route(Motor):
    def __init__(self, a, b, c, d) -> None:
        self.ListOfMotors = [a, b, c, d]    # Список экземпляров класса Motor
        self.xy_speeds = [0, 0]             # Скорости (x, y) для всего робота
        self.setUpI2C()                     # Инициализация пинов I2C

    def setUpI2C(self) -> None:
        ```
        Инициализация I2C
        ```
        GPIO.setwarnings(False)
        self.i2c = board.I2C()
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 100
        self.PredArrForMove = [0,0,0,0]

    def _revers_potate(self, FuncOfAngel) -> None:
        ```
        Расчёт скоростей (x, y) из скоростей колёс (a, b, c, d)
        ```
        x = (self.ListOfMotors[0] - self.ListOfMotors[2] - 2*Motor.L*FuncOfAngel)*0.5
        y = (self.ListOfMotors[1] - self.ListOfMotors[3] - 2*Motor.L*FuncOfAngel)*0.5
        self.xy_speeds = [x, y]

    def _front_potate(self, ModeOfAngles, FuncOfAngel) -> None:
        ```
        Расчёт скоростей колёс (экземпляров) из скоростей (x, y)
        ```
        for i in self.ListOfMotors:
            i._single_front_potate(self.xy_speeds, self.__differencial(ModeOfAngles, FuncOfAngel))

    def set_speed(self, *args, ModeOfAngles = 0, FuncOfAngel = 0, turnOsSys = 0) -> list:
        ```
        Расчёт скорости колеса (экземпляра) из скоростей (x, y)
        ```
        if turnOsSys:
            # Пересчёт скоростей (x, y), если нужен поворот оси
            args = self.potateOfSys(args[0],args[1],deg2rad(turnOsSys))
        
        self.xy_speeds = args
        self._front_potate(ModeOfAngles, FuncOfAngel)
        
        # Возвращает массив скоростей колёс
        return(self.getAllMotorsSpeeds())

    def getAllMotorsSpeeds(self) -> list:
        ```
        Возвращает массив скоростей колёс
        ```
        res = []
        for i in self.ListOfMotors:
            res.append(round(i.speed, 2))
        return(res)

    @staticmethod
    def __differencial(mode, args) -> float:
        ```
        Статичный метод для численного диференцирования (для поворота)
        ```
        if not mode:
            return 0
        else:
            dif = (args[1]-args[0])/(0.5)
        return dif
    
    @staticmethod
    def potateOfSys(a,b,alfa) -> list:
        ```
        Статичный метод для вращения точек (a,b) на угол alfa
        ```
        pole_phi =0
        if a and b:
            pole_phi = atan(b/a)
            if a < 0: pole_phi = pole_phi + 3.14
        elif a == 0:
            if b > 0: pole_phi = deg2rad(90)
            if b < 0: pole_phi = deg2rad(270)
        elif b == 0:
            if a > 0: pole_phi = deg2rad(0)
            if a < 0: pole_phi = deg2rad(180)
        else: 
            rospy.logerr("ERROR INCORRECT DATA")
            return([0, 0])
        pole_len = ((a**2+b**2)**0.5)/(2**0.5)
            
        xr = round(pole_len*cos(pole_phi+alfa), 2)
        yr = round(pole_len*sin(pole_phi+alfa), 2)
        return([xr, yr])
            
    def move(self, SpeedsMotors, preSpeedsMotors, numsPins) -> None:
        ```
        Поиск максимальной скорости.
        Перерасчёт  остальных под единицу.
        Передача скоростей на моторы.
        ```
        # logwarn("Speeds: %s; PreSpeed: %s", SpeedsMotors, preSpeedsMotors)
        # Передача скоростей моторам
        maxSpeed = max(max(SpeedsMotors), abs(min(SpeedsMotors)))
        if maxSpeed: SpeedsMotors = array(SpeedsMotors)/maxSpeed
            
        for n, i in enumerate(self.ListOfMotors):
            try: 
                i.set_speed_shim(int(hex(int(abs(SpeedsMotors[n]**4)*65535)), 16))
            #     Speed[i] = int(hex(int(abs(arrOfSpeeds[i]/(arrOfSpeeds[i]-preArr[i]))*65535)), 16)
            #     Speed[i] = int(hex(int(abs(arrOfSpeeds[i]**2 + ((arrOfSpeeds[i]-preArr[i])*0))*65535)), 16)
            except: 
                logerr("ERROR OF MATH")
                print(int(hex(int(abs(SpeedsMotors[n]**4)*65535)), 16))
        
        self.pca.channels[numsPins[0]].duty_cycle = self.ListOfMotors[0].speed_shim
        self.pca.channels[numsPins[1]].duty_cycle = int(SpeedsMotors[0] > 0)*65535
        self.pca.channels[numsPins[2]].duty_cycle = int(SpeedsMotors[0] < 0)*65535
        
        self.pca.channels[numsPins[3]].duty_cycle = self.ListOfMotors[1].speed_shim
        self.pca.channels[numsPins[4]].duty_cycle = int(SpeedsMotors[1] > 0)*65535
        self.pca.channels[numsPins[5]].duty_cycle = int(SpeedsMotors[1] < 0)*65535
        
        self.pca.channels[numsPins[6]].duty_cycle = self.ListOfMotors[2].speed_shim
        self.pca.channels[numsPins[7]].duty_cycle = int(SpeedsMotors[2] > 0)*65535
        self.pca.channels[numsPins[8]].duty_cycle = int(SpeedsMotors[2] < 0)*65535
        
        self.pca.channels[numsPins[9]].duty_cycle = self.ListOfMotors[3].speed_shim
        self.pca.channels[numsPins[10]].duty_cycle = int(SpeedsMotors[3] > 0)*65535
        self.pca.channels[numsPins[11]].duty_cycle = int(SpeedsMotors[3] < 0)*65535        


def main() -> None:
    ```
    Тестовая часть программы.
    Проверка работоспособности методов
    ```
    A = Motor(1,   0)
    B = Motor(0,   1)
    C = Motor(-1,  0)
    D = Motor(0,  -1)
    abcd = Route(A, B, C, D)
    angle = 315
    listTest = [[0.5,0],[-0.5,0]]
    for i in listTest:
        joy = i
        print(abcd.set_speed(joy[0], joy[1], turnOsSys=angle))

if __name__=="__main__":
    main()
