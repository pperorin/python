import math
class Spherical:

    def __init__(self,r):
        self.r=r

    def changeR(self,Radius):
        self.r=Radius

    def findVolume(self):
        fv="%18s" %(4/3*math.pi*self.r*self.r*self.r)
        return fv

    def findArea(self):
        fa="%18s" %(4*math.pi*self.r*self.r)
        return fa

    def __str__(self):
        return "Radius =" + str(self.r) + " Volumn = " + self.findVolume() + " Area = " + self.findArea()

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)