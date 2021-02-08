# encoding: utf-8
from random import randint
import psutil
import time
import os

process = psutil.Process(os.getpid())
"""
version sans recursivite
"""

def plus_grande_sequence(E):
    if len(E) == 0:
        return E

    precedent = [-1 for e in E]
    longueur  = [0 for e in E]

    longueur[0] = 1
    for k in range(1, len(E)):

        bestL = 1
        bestP = -1

        for j in range(0,k) :
            if E[k] >= E [ j ] and longueur[j]+1 > bestL:
                bestL = longueur [j]+1
                bestP = j

        precedent[k] = bestP
        longueur[k] = bestL

    # on récupère la longueur de la plus grande séquence
    maxiL = 0
    for i,l in enumerate(longueur):
        if l > longueur[maxiL]:
            maxiL = i

    # on récupère la plus grande séquence
    seq = [maxiL]
    while precedent[seq[-1]] != -1:
        p = precedent[seq[-1]]
        seq.append(p)

    seq.reverse()
    return seq

l=[]
for i in range(900):
	l.append(randint(0,2000))
	
#E = [10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 1, 15, 6, 11, 0, 14, 7, 9]
E=l
b = plus_grande_sequence(E)
print("E",E)
print("indice:",b)
print("valeurs:", [ E[i] for i in b ])



print("\ninformation process\n")
print(process.memory_info().rss)
print(process.memory_info()[0])




