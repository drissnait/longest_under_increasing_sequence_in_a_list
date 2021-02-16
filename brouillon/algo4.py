# encoding: utf-8
from random import randint
import time
import psutil
import os
import random
import timeit
import sys


start_time=time.time()
def plus_longue_sequence(l):
	plusGrandeSousSequence=[]
	lMax=0
	for i in range (len(l)):
		k=1
		while(k<len(l)):
			j=i+k
			valActuel=l[i]
			liste=[]
			liste.append(l[i])
			while(j<len(l)):
				if(l[j]>valActuel):
					#print(str(l[j])+">"+str(l[i]))
					valActuel=l[j]
					liste.append(valActuel)
				j+=1
				print(liste)
				if (len(liste)>lMax):
					plusGrandeSousSequence=liste
					lMax=len(liste)
			k+=1
			
	print("plus longue sous sequence est : ")
	print(plusGrandeSousSequence)
		
l=[5,1,3,9]
plus_longue_sequence(l)
execution_time=time.time() - start_time
print("---Temps d'execution:  %s seconds ---" + str(execution_time))
