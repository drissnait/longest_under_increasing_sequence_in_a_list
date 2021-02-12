# encoding: utf-8
from random import randint
import time
import psutil
import os
import random
import timeit
import sys
from test import *

process = psutil.Process(os.getpid())
sys.setrecursionlimit(10000)

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
    #S contient les sequences obtenues, on cherche a avoir la plus grande dans le tableau
    S = indexes(liste)
    plusLongue = []
    #recherche de la plus longue sequence 
    for s in S:
        if len(s) > len(plusLongue):
            plusLongue = s
    return plusLongue


#Creer une liste de 3000 elements aléatoires sur lequel on fera le test
l=[]
for i in range(3000):
	l.append(randint(0,100000))
#E = [10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 1, 15, 6, 11, 0, 14, 7, 9]
E=l
b = plus_longue_sequence_croissante(E)
print("Plus longue sequence :", [ E[i] for i in b ])
mem = process.memory_info()[0] / float(2 ** 20)
print("consommation mémoire en MB :",mem,"Mb")
print("\n")

"""Transfer les résultats de verification de croissance de liste dans un fichier.dat"""
fileTest=open("../resultat_test/resultat_test_algo1.dat","a")
if(verifier_croissance(b)==True):
	fileTest.write("1")
	fileTest.write("\n")
else:
	fileTest.write("0")
fileTest.close()




execution_time=time.time() - start_time
print("---Temps d'execution:  %s seconds ---" + str(execution_time))

"""Transfer des donnees d'execution dans les fichiers .dat """
file=open("../data/data_algo1_time.dat","a")
file.write(str(execution_time))
file.write("\n")
file.close()

file=open("../data/data_algo1_memory.dat","a")
file.write(str(mem))
file.write("\n")
file.close()
