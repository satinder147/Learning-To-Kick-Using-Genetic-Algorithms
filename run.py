import random
from obj import dna

instances=[]
for i in range(4):
    instances.append(dna())

while True:
    for i in range(len(instances)):
        instances[i].fitness(i)

    break
