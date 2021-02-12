# encoding: utf-8
from random import randint
import time
import psutil
import os
import random
import timeit
import sys

process = psutil.Process(os.getpid())
sys.setrecursionlimit(10000000)

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
            if len(s) > len(plusLongue) and liste[k] > liste [s[-1]]:
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
for i in range(5000):
	l.append(randint(0,10000))
E = [10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 1, 15, 6, 11, 0, 14, 7, 9,18,29,9,3,57,92,4,182,34,58,2,3,472,502,382,594,90]
#E=l
b = plus_longue_sequence_croissante(E)
print("E",E)
print("indice:",b)
print("\n\n")
print("valeurs:", [ E[i] for i in b ])
mem = process.memory_info()[0] / float(2 ** 20)
print("consommation mémoire en MB :",mem,"Mb")
print("\n")

execution_time=time.time() - start_time
print("---Temps d'execution:  %s seconds ---" + str(execution_time))
