# encoding: utf-8
from random import randint
import time
import psutil
import os
import random
import timeit

process = psutil.Process(os.getpid())

start_time=time.time()
def indexes(liste, k=None):
    if k is None:
        k = len(E)-1
    if k == 0:
        return [[0]]
    else :
        S = indexes(liste, k-1)
        plusLongue = []
        for j,s in enumerate(S):
            if len(s) > len(plusLongue) and liste[k] >= liste [s[-1]]:
                plusLongue = s
        plusLongue = plusLongue + [k]
        S.append(plusLongue)
        return S

def plus_longue_sequence_croissante(liste):
    if len(liste) == 0:
        print ("ERREUR: La liste ne contient aucun élement")
        return E
    S = indexes(liste)
    plusLongue = []
    for s in S:
        if len(s) > len(plusLongue):
            plusLongue = s
    return plusLongue

l=[]
for i in range(30):
	l.append(randint(0,2000))
E = [10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 1, 15, 6, 11, 0, 14, 7, 9]
#E= [10,80, 5, 0, 7, 8, 9, 10, 4,12]
#E=[10,80,70,3,50,40,98,4,0,3]
#E=l
b = plus_longue_sequence_croissante(E)
print("E",E)
print("indice:",b)
print("\n\n")
print("valeurs:", [ E[i] for i in b ])
print("\ninformation process")
#print(process.memory_info().rss/1024)

mem = process.memory_info()[0] / float(2 ** 20)
print("consommation mémoire en MB :",mem,"Mb")
print("\n")

execution_time=time.time() - start_time
print("---Temps d'execution:  %s seconds ---" + str(execution_time))

"""mem_resource = []
for i in range(1, 21):
    a = np.zeros((1000 * i, 100 * i))
    mem_resource.append(memory_usage_resource())

print(mem_resource)"""


