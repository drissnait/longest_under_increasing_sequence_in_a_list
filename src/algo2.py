# encoding: utf-8
from random import randint
import psutil
import time
import os
from test import *

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
            if liste[k] >= liste [ j ] and longueur[j]+1 > toplength:
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
    #les elements sont stockes dans la liste en commencant par la plus grande valeur, on inverse donc la sous sequence
    seq.reverse()
    return seq

#Creation de la liste ed 3000 elements sur laquelle on fera nos tests
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
execution_time=time.time() - start_time
print("---Temps d'execution:  %s seconds ---" +str(execution_time))


"""Transfer les résultats de verification de croissance de liste dans un fichier.dat"""
fileTest=open("../resultat_test/resultat_test_algo2.dat","a")
if(verifier_croissance(b)==True):
	fileTest.write("1")
	fileTest.write("\n")
else:
	fileTest.write("0")
fileTest.close()

"""Transfer des donnees d'execution dans les fichiers .dat """
file=open("../data/data_algo2_time.dat","a")
file.write(str(execution_time))
file.write("\n")
file.close()

file=open("../data/data_algo2_memory.dat","a")
file.write(str(mem))
file.write("\n")
file.close()
