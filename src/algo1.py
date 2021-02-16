# encoding: utf-8
import time
import psutil
import os
from test import *


def plus_longue_sequence_recursif(liste):
	max_sequence = []
	for i in range(len(liste)):
		sequence = plus_longue_sequence_a_partir_du_premier_element(liste[i:len(liste)])
		if(len(sequence) > len(max_sequence)):
			max_sequence = sequence
	return max_sequence

def plus_longue_sequence_a_partir_du_premier_element(liste):
	result = [liste[0]]
	for i in range(1, len(liste)):
		if(liste[i] > liste[0]):
			sequence = [liste[0]] + plus_longue_sequence_a_partir_du_premier_element(liste[i: len(liste)])
			if(len(sequence) > len(result)):
				result = sequence
	return result


liste=[10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 52, 24, 123, 348, 1324, 12, 43, 124, 554, 23, 432, 398, 234, 3432]
#Pour l'espace memoire
process = psutil.Process(os.getpid())
#Pour le temps d'execution
start_time=time.time()
res=plus_longue_sequence_recursif(liste)
execution_time=time.time() - start_time
mem = process.memory_info()[0] / float(2 ** 20)
print("Plus longue sequence : "+str(res))




"""Transfer les résultats de verification de croissance de liste dans un fichier.dat"""
fileTest=open("../resultat_test/resultat_test_algo1.dat","a")
if(verifier_croissance(res)==True):
	fileTest.write("1")
	fileTest.write("\n")
else:
	fileTest.write("0")
fileTest.close()






"""Transfer des donnees d'execution dans les fichiers .dat """
file=open("../data/data_algo1_time.dat","a")
file.write(str(execution_time))
file.write("\n")
file.close()

file=open("../data/data_algo1_memory.dat","a")
file.write(str(mem))
file.write("\n")
file.close()
