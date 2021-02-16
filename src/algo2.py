# encoding: utf-8
import time
import psutil
import os
from test import *


class ListItem:
    def __init__(self, item, position):
        self.item = item
        self.position = position

def plus_longue_sequence_iteratif(liste):
	elements_to_process = []
	for i in range(len(liste)):
		elements_to_process.append([ListItem(liste[i], i)])
	longest_sequence = []
	while elements_to_process:
		element = elements_to_process.pop()
		for i in range(element[len(element) - 1].position + 1, len(liste)):
			for j in range(i, len(liste)):
				if liste[j] > element[len(element) - 1].item:
					elements_to_process.append(element + [ListItem(liste[j], j)])
					if len(longest_sequence) < len(element) + 1:
						longest_sequence = element + [ListItem(liste[j], j)]
						
	return list(map(lambda list_item: list_item.item, longest_sequence))


liste=[10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 52, 24, 123, 348, 1324, 12, 43, 124, 554, 23, 432, 398, 234, 3432]
#pour l'espace memoire
process = psutil.Process(os.getpid())
#pour le temps d'execution
start_time=time.time()
res=plus_longue_sequence_iteratif(liste)
execution_time=time.time() - start_time
mem = process.memory_info()[0] / float(2 ** 20)

print("Plus longue sequence : "+str(res))


"""Transfer les résultats de verification de croissance de liste dans un fichier.dat"""
fileTest=open("../resultat_test/resultat_test_algo2.dat","a")
if(verifier_croissance(res)==True):
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
