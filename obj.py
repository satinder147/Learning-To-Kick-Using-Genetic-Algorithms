import random
from ard import arduino
ar=arduino()
class dna:
    def __init__(self):
        self.motor1=random.randrange(1,24)
        self.motor2=random.randrange(1,24)
    def fitness(self,instance_no):
        ar.mov(self.motor1,instance_no,1)
        ar.mov(self.motor2,instance_no,2)
