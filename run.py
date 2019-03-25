import random
import cv2
from ard import arduino
from obj import dna
import time
ar=arduino()
def reset():
    global ar
    ar.mov(0,0,0)
    ar.mov(0,0,0)
    time.sleep(2)
    ar.mov(12,0,1)
    time.sleep(2)
    ar.mov(0,1,0)
    time.sleep(2)
    ar.mov(12,1,1)
    time.sleep(2)
    ar.mov(0,2,0)
    time.sleep(2)
    ar.mov(12,2,1)
    time.sleep(2)
    ar.mov(3,3,0)
    time.sleep(2)
    ar.mov(12,3,1)
    time.sleep(2)
p=0
reset()
cap=cv2.VideoCapture(0)
#r,f=cap.read()
#cv2.imshow('s',f)
#cv2.waitKey(0)
instances=[]
for i in range(4):
    instances.append(dna())
    print(instances[i].motor1,instances[i].motor2)
while True:
    rt=cap.read()[1]
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
    reset()
    p=p+1
    print('generation '+str(p)+' completed')
    #cv2.imshow("final",rt)
    #cv2.waitKey(1)
    #time.sleep(10)
