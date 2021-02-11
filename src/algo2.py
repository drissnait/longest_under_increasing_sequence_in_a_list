# encoding: utf-8
from random import randint
import psutil
import time
import os

process = psutil.Process(os.getpid())
"""
version sans recursivite
"""
start_time=time.time()

def get_plus_longue_sequence(longueur,longueurMax):
	for i,l in enumerate(longueur):
		if l > longueur[longueurMax]:
		    longueurMax = i
	return longueurMax
def plus_longue_sequence_croissante(E):
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

    # longueurMax est l'element max du tableau longueur qui contient les longueurs des differentes sous sequences
    longueurMax=get_plus_longue_sequence(longueur,0)

    # on récupère la plus grande séquence
    seq = [longueurMax]

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
b = plus_longue_sequence_croissante(E)
print("Plus longue sequence :", [ E[i] for i in b ])
mem = process.memory_info()[0] / float(2 ** 20)
print("consommation mémoire en MB :",mem,"Mb")
print("\n")
execution_time=time.time() - start_time
print("---Temps d'execution:  %s seconds ---" +str(execution_time))

"""Transfer des donnees d'execution dans les fichiers .dat """
file=open("../data/data_algo2_time.dat","a")
file.write(str(execution_time))
file.write("\n")
file.close()

file=open("../data/data_algo2_memory.dat","a")
file.write(str(mem))
file.write("\n")
file.close()
