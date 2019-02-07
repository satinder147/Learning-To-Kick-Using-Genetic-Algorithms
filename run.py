import random
import cv2
from ard import arduino
from obj import dna
import time
ar=arduino()
cap=cv2.VideoCapture(1)
instances=[]
for i in range(4):
    instances.append(dna())
    print(instances[i].motor1,instances[i].motor2)
while True:
    for i in range(len(instances)):
        instances[i].fitness(i,cap)
        time.sleep(2)
    matpool=[]
    for i in range(len(instances)):
        n=int(instances[i].fitnes*100)
        for _ in range(n):
            matpool.append(instances[i])
    for i in range(4):
        a=random.randrange(len(matpool))
        b=random.randrange(len(matpool))
        instances[i]=instances[i].cross(matpool[a],matpool[b])
    ar.mov(12,4,1)
    time.sleep(10)
