import random
from ard import arduino
from ball_tracking import *
import time

ar=arduino()


def getSegments(frame):
    l=[]
    l.append(frame[360:430,:])
    l.append(frame[278:360,:])
    l.append(frame[207:278,:])
    l.append(frame[135:210,:])
    return l


class dna:
    def __init__(self):
        self.motor1=random.randrange(1,25)
        self.motor2=random.randrange(1,25)
        self.fitnes=0
    def fitness(self,instance_no,cap):
        ar.mov(self.motor2,instance_no,1)
        time.sleep(2)
        ar.mov(self.motor1,instance_no,0)
        time.sleep(2)

        frame=cap.read()[1]
        print("reached")
        frames=getSegments(frame)
        self.fitnes=getFitness(frames[instance_no])
        #print(self.fitnes)

    def cross(self,a,b):
        child=dna()
        if(random.uniform(0,1)<0.05):
            child.motor1=random.randrange(1,24)
            child.motor2=random.randrange(1,24)
        else:
            child.motor1=(a.motor1*a.fitnes+b.motor1*b.fitnes)/(a.fitnes+b.fitnes)
            child.motor2=(a.motor2*a.fitnes+b.motor2*b.fitnes)/(a.fitnes+b.fitnes)


        return child
