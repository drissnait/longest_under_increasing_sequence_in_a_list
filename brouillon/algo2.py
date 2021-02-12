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
def plus_longue_sequence_croissante(liste):
    if len(liste) == 0:
        return liste

    precedent = [-1 for e in liste]
    longueur  = [0 for e in liste]

    longueur[0] = 1
    k=1
    while(k<len(liste)):
        toplength = 1
        toppredecesseur = -1
        for j in range(0,k) :
            if liste[k] > liste [ j ] and longueur[j]+1 > toplength:
                toplength = longueur [j]+1
                toppredecesseur = j    
        
        precedent[k] = toppredecesseur
        longueur[k] = toplength
        k+=1

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
for i in range(5000):
	l.append(randint(0,100000))
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
print("---Temps d'execution:  %s seconds ---" +str(execution_time))

