# encoding: utf-8
from random import randint
import psutil
import time
import os
from test import *



def plus_grande_sequence_wikipedia(E):
    P = [-1 for m in E]
    M = [-1 for n in E]
    L = 0
    for i in range(0, len(E)):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if E[M[mid]] < E[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        newL = lo
        P[i] = M[newL - 1]

        if newL > L:
            M[newL] = i
            L = newL
        elif E[i] < E[M[newL]]:
            M[newL] = i
    S = [-1 for i in range(L)]
    k = M[L]
    for i in range(L-1, -1, -1) :
        S[i] = k
        k = P[k]
    return S
  

#Creation de la liste ed 3000 elements sur laquelle on fera nos tests
l=[10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 52, 24, 123, 348, 1324, 12, 43, 124, 554, 23, 432, 398, 234, 3432]
#espace memoire
process = psutil.Process(os.getpid())
#temps d'execution
start_time=time.time()
res = plus_grande_sequence_wikipedia(l)
execution_time=time.time() - start_time
mem = process.memory_info()[0] / float(2 ** 20)

print("Plus longue sequence :", [ l[i] for i in res ])


"""Transfer les résultats de verification de croissance de liste dans un fichier.dat"""
fileTest=open("../resultat_test/resultat_test_algo3.dat","a")
if(verifier_croissance(res)==True):
	fileTest.write("1")
	fileTest.write("\n")
else:
	fileTest.write("0")
fileTest.close()

"""Transfer des donnees d'execution dans les fichiers .dat """
file=open("../data/data_algo3_time.dat","a")
file.write(str(execution_time))
file.write("\n")
file.close()

file=open("../data/data_algo3_memory.dat","a")
file.write(str(mem))
file.write("\n")
file.close()
