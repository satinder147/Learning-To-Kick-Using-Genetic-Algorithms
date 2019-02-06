import random
import cv2
from obj import dna
cap=cv2.VideoCapture(1)
instances=[]
for i in range(4):
    instances.append(dna())
while True:
    for i in range(len(instances)):
        instances[i].fitness(i,cap)
    matpool=[]
    for i in range(len(instances)):
        n=int(instance[i].fitnes*100)
        for _ in range(n):
            matpool.append(instance[i])
    for i in range(4):
        a=random.randrange(len(matpool))
        b=random.randrange(len(matpool))
        instance[i]=instance[i].cross(matpool[a],,matpool[b])
