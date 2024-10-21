from math import atan, pi, acos
from numpy import zeros, rad2deg

class potateKinem():
    def __init__(self, l0, l1) -> None:
        self.l0 = l0
        self.l1 = l1
    
    def computeDecart(self, x, y, z):
        r = (x**2 + y**2 + z**2)**0.5
        theta = atan((x**2 + y**2)**0.5/z)
        fi = atan(y/x)
        return self.computePolar(r, theta, fi)

    def computePolar(self, r, theta, fi):
        print("Debug 1:", r, rad2deg(theta), rad2deg(fi))
        if r > self.l0 + self.l1:
            print("ERROR")
            return None
        angls = zeros(3)
        if fi < pi:
            angls[0] = fi
        else: angls[0] = pi - fi
        if r > self.l0 + self.l1:
            angls[1] = pi - theta
            angls[2] = pi
        else:
            angls[1] = acos((self.l0**2 - self.l1**2 + r**2)/(2*self.l0*r))
            angls[2] = acos((self.l0**2 + self.l1**2 - r**2)/(2*self.l0*self.l1))
        return angls

def main():
    Ob = potateKinem(1,1)
    print(Ob.computeDecart(1.125, 0.64951905, 0.75))

if __name__=="__main__":
    main()