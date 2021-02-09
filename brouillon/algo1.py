# encoding: utf-8
from random import randint
import time
import psutil
import os
import random
import timeit

process = psutil.Process(os.getpid())

start_time=time.time()
def plus_grande_sequence_position_k(E, k=None):
    if k is None:
        k = len(E)-1
    if k == 0:
        return [[0]]
    else :
        S = plus_grande_sequence_position_k(E, k-1)

        best = []
        for j,s in enumerate(S):
            if len(s) > len(best) and E[k] >= E [s[-1]]:
                best = s
        best = best + [k]
        S.append(best)
        return S

def plus_grande_sequence(E):
    if len(E) == 0:
        return E
    S = plus_grande_sequence_position_k(E)
    best = []
    for s in S:
        if len(s) > len(best):
            best = s
    return best

l=[]
for i in range(30):
	l.append(randint(0,2000))
#E = [10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 1, 15, 6, 11, 0, 14, 7, 9]
E=l
b = plus_grande_sequence(E)
print("E",E)
print("indice:",b)
print("\n\n")
print("valeurs:", [ E[i] for i in b ])
print("\ninformation process")
#print(process.memory_info().rss/1024)

mem = process.memory_info()[0] / float(2 ** 20)
print(mem)
print("\n")

execution_time=time.time() - start_time
print("---Temps d'execution:  %s seconds ---" + str(execution_time))

"""mem_resource = []
for i in range(1, 21):
    a = np.zeros((1000 * i, 100 * i))
    mem_resource.append(memory_usage_resource())

print(mem_resource)"""


