#!/usr/bin/python3 

from math import pi, cos, sin, atan2, atan, acos
from numpy import zeros, matmul, deg2rad, array, ndarray, rad2deg
from typing import Union, Any, Optional
# from matplotlib.pyplot import plot, show, subplot, figure
from rospy import loginfo, logwarn, logerr

class data():
    def __init__(self, a1: Optional [int]=10,  s1: Optional [int]=36, 
                       l1: Optional [int]=178, l2: Optional [int]=159.8, 
                       s4: Optional [int]=10,  s5: Optional [int]=135, 
                       q=array([0,0,0,0,0]),   l4: Optional [int]=125) -> None:
        """
        Класс для хранения данных о манипуляторе
        """
        self.slovar = dict()
        self.slovar["a1"] = a1
        self.slovar["s1"] = s1
        self.slovar["l1"] = l1
        self.slovar["l2"] = l2
        self.slovar["s4"] = s4
        self.slovar["s5"] = s5
        self.slovar["l4"] = l4
        self.slovar["q"] = q
        self.slovar["DH"] = self.calculationOfDH(q)

    def calculationOfDH(self, new_q: array):
        """
        Вычисление параметров Денавита-Хартенберга
        """
        self.slovar["q"] = new_q
        DH = [[self.slovar["a1"],  self.slovar["l1"], self.slovar["l2"], 0,                 0],                 # a     |0
             [pi/2,                0,                 0,                 pi/2,              0],                 # alfa  |1
             [self.slovar["s1"],   0,                 0,                 self.slovar["s4"], self.slovar["s5"]], # d     |2
             [new_q[0],            new_q[1],          new_q[2],          new_q[3]+pi/2,     new_q[4]]]          # theta |3
        self.slovar["DH"] = DH
        return DH

    def get_data(self, *names: str) -> Union [float, int, list]:
        """
        Возвращает значение из общего словаря по его имени: a1, s1, l1, l2, s4, s5, q, DH
        """
        res = []
        for i in names:
            res.append(self.slovar[i])
        return res

class baseCalculations(data):
    def __init__(self, a1: Optional [int]=10,  s1: Optional [int]=36, 
                       l1: Optional [int]=178, l2: Optional [int]=159.8, 
                       s4: Optional [int]=10,  s5: Optional [int]=135, 
                       q=array([0,0,0,0,0]),   l4: Optional [int]=125) -> None:
        """
        Класс для базовых вычислений для манипулятора
        """
        super().__init__(a1, s1, l1, l2, s4, s5, q)
        self.T = zeros((5,4,4))
        for i in range(5):
            a = 0
            alfa = 1
            d = 2
            theta = 3
            for j in range(4):
                self.T[i] = [
                    # [0]
                        [cos(self.slovar["DH"][theta][j]), 
                         -cos(self.slovar["DH"][alfa][j])*sin(self.slovar["DH"][theta][j]),
                         sin(self.slovar["DH"][alfa][j])*sin(self.slovar["DH"][theta][j]),
                         self.slovar["DH"][a][j]*cos(self.slovar["DH"][theta][j])],
                    # [1]
                        [sin(self.slovar["DH"][theta][j]), 
                         cos(self.slovar["DH"][alfa][j])*cos(self.slovar["DH"][theta][j]),
                         -sin(self.slovar["DH"][alfa][j])*cos(self.slovar["DH"][theta][j]),
                         self.slovar["DH"][a][j]*sin(self.slovar["DH"][theta][j])],
                    # [2]
                        [0,                 
                         sin(self.slovar["DH"][alfa][j]),
                         cos(self.slovar["DH"][alfa][j]),                  
                         self.slovar["DH"][d][j]],
                    # [3]
                        [0, 0, 0, 1]]
        
    def calculationOfT(self, mode:int) -> array:
        """
        Вычисление матрицы однородного преобразования (Т) (mode 0: от 0 СК до 3 СК (Т_0->3), mode 3: от 3 СК до 0 СК (Т_3->0))
        """
        if mode == 0:
            return matmul(matmul(matmul(self.T[0], self.T[1]), self.T[2]), self.T[3])
        elif mode == 3:
            return matmul(matmul(matmul(self.T[3], self.T[2]), self.T[1]), self.T[0])
        else:
            return "incorrect data"
    
    def calculationOfR(self, mode:int) -> array:
        """
        Вычисление матрицы вращения (0: Т_0->3, 3: Т_3->0)
        """
        fromT = self.calculationOfT(mode)
        return ([[fromT[0][0], fromT[0][1], fromT[0][2]],
                    [fromT[1][0], fromT[1][1], fromT[1][2]],
                    [fromT[2][0], fromT[2][1], fromT[2][2]]])
    
    def calculationOfP(self, mode:int) -> array:
        """
        Вычисление вектора (0: Т_0->3, 3: Т_3->0)
        """
        fromT = self.calculationOfT(mode)
        return ([[fromT[0][-1]], [fromT[1][-1]], [fromT[2][-1]]])
    
    def getT(self, num:Union [int, None] = None) -> array:
        """
        Возвращает значения матрицы однородного преобразования по индексу, где индекс соответствует СК
        """
        try: return self.T[num]
        except: 
            logwarn("incorrect data. returned all array <T>:")
            return self.T
        
    def EulersAngles(self, angles: list=[0,0,0]):
        """
        Вычисление углов Эйлера
        """
        # fi, theta, ksi
        R_elera = [
                    # [0]
                    [cos(angles[0])*cos(angles[1])*cos(angles[2]) - sin(angles[0])*sin(angles[2]),
                    -cos(angles[0])*cos(angles[1])*sin(angles[2]) - sin(angles[0])*cos(angles[2]),
                    cos(angles[0])*sin(angles[1])],
                    # [1]
                    [sin(angles[0])*cos(angles[1])*cos(angles[2]) + cos(angles[0])*sin(angles[2]),
                    -sin(angles[0])*cos(angles[1])*sin(angles[2]) + cos(angles[0])*cos(angles[2]),
                    sin(angles[0])*sin(angles[1])],
                    # [2]
                    [-sin(angles[1])*cos(angles[2]),
                    sin(angles[1])*sin(angles[2]),
                    cos(angles[1])]
                    ]
        return R_elera

    def anglesFromEuler(self, R: array):
        """
        Прямая кинематика (из матрицы однородного преобразования в углы эйлера)
        """
        angels = [None,None,None] # fi, theta, ksi
        match = R[2][2]
        if match == 1: # 2
            angels[1] = 0
            sum = atan2(R[1][0],R[0][0])
            angels[0] = sum/2
            angels[2] = sum/2
        elif match == -1: # 3
            angels[1] = pi
            dif = atan2(-R[0][1],-R[0][0])
            angels[0] = dif/2
            angels[2] = dif/2
        else:
            try:    
                angels[1] = atan2((1-R[2][2]**2)**0.5, R[2][2])
                angels[0] = atan2(R[1][2], R[0][2])
                angels[2] = atan2(R[2][1], -R[2][0])
            except:
                angels[1] = atan2(-(1-R[2][2]**2)**0.5, R[2][2])
                angels[0] = atan2(-R[1][2], -R[0][2])
                angels[2] = atan2(-R[2][1], R[2][0])
        return angels

        
    @staticmethod
    def print_array(array: list, numOfRound = 0):
        """
        Метод для красивого вывода любого массива (вектора)
        """
        try:
            len(array[0])
            try: 
                len(array[0][0])
                for i in range(len(array[0])):
                    print("|", end='')
                    for j in range(len(array[0][0])):
                        if numOfRound:
                            print(round(array[0][i][j], numOfRound), end=',\t')
                        else:
                            print(array[0][i][j], end=',\t')
                    print("|")
            except:
                for i in range(len(array)):
                    print("|", end='')
                    for j in range(len(array[0])):
                        if numOfRound:
                            print(round(array[i][j], numOfRound), end=',\t')
                        else:
                            print(array[i][j], end=',\t')
                    print("|")
        except:
            loginfo("vector detected")
            print("|", end='')
            for i in range(len(array)):
                if numOfRound:
                    print(array[i])
                    print(round(array[i], numOfRound), end=',\t')
                else:
                    print(array[i], end=',\t')
            print("|")

class reversPotate(data):
    def __init__(self, a1: Optional [int]=10,  s1: Optional [int]=36, 
                       l1: Optional [int]=178, l2: Optional [int]=159.8, 
                       s4: Optional [int]=10,  s5: Optional [int]=135, 
                       q=array([0,0,0,0,0]),   l4: Optional [int]=125) -> None:
        super().__init__(a1, s1, l1, l2, s4, s5, q)
    def Euler2Dekart(self, angels):
        x = cos(angels[0])
        y = cos(angels[1])
        z = cos(angels[2])
        return [x,y,z]
    def calculationOfPotate(self, x, y, z):
        k = (x**2+y**2)**0.5
        zr = z + self.slovar["l4"] - self.slovar["s1"]
        d = (k**2+zr**2)**0.5
        try:
            self.slovar["q"][0] = atan(y/x) # angle 1
            self.slovar["q"][1] = (pi/2)-(atan(zr/k)+acos((d**2+self.slovar["l1"]**2-self.slovar["l2"]**2)/(2*d*self.slovar["l1"]))) # angle 2
            self.slovar["q"][2] = pi-acos((-d**2+self.slovar["l1"]**2+self.slovar["l2"]**2)/(2*self.slovar["l1"]*self.slovar["l2"])) # angle 3
            self.slovar["q"][3] = pi-(self.slovar["q"][1] + self.slovar["q"][2]) # angle 4
        except:
            logerr("Attention! Singularity has been reached. Calculations stopped")
def main():
    while True:
        motors = reversPotate()
        x, y, z = input("Введите 3 числа от -0.9 до 1: ")
        if (x < -0.9): x = -0.9
        if (x > 1): x = 1
        if (y < -0.9): y = -0.9
        if (y > 1): y = 1
        if (z < -0.9): z = -0.9
        if (z > 1): z = 1
            
        motors.calculationOfPotate(x, y, z)
        print(self.slovar["q"])
        
        i2c = board.I2C()  # uses board.SCL and board.SDA
        pca = PCA9685(startServs.i2c)
        pca.frequency = 50
        servo10 = servo.Servo(pca.channels[10], actuation_range = 180, min_pulse = 750, max_pulse=2250)
        servo11 = servo.Servo(pca.channels[11], actuation_range = 180, min_pulse = 750, max_pulse=2250)
        servo12 = servo.Servo(pca.channels[12], actuation_range = 180, min_pulse = 750, max_pulse=2250)
        servo13 = servo.Servo(pca.channels[13], actuation_range = 180, min_pulse = 750, max_pulse=2250)
        servo14 = servo.Servo(pca.channels[14], actuation_range = 180, min_pulse = 750, max_pulse=2250)
        # servo15 = servo.Servo(pca.channels[15], actuation_range = 180, min_pulse = 750, max_pulse=2250)
        rospy.init_node('Servos')
        # rospy.Subscriber("joy", Joy, self.callback_joy)
        
        servo10.angle = self.slovar["q"][0]
        servo11.angle = self.slovar["q"][1]
        servo12.angle = self.slovar["q"][2]
        servo13.angle = self.slovar["q"][3]
        servo14.angle = self.slovar["q"][4]
        # servo15.angle = self.slovar["q"][5]
    
if __name__=="__main__":
    main()
