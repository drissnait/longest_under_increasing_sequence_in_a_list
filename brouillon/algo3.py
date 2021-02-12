# encoding: utf-8
from random import randint
import psutil
import time
import os

process = psutil.Process(os.getpid())
start_time=time.time()
def plus_grande_sequence_wikipedia(E):
    P = [-1 for _ in E] 
    M = [-1 for _ in E]

    L = 0
    for i in range(0, len(E)-1):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if E[M[mid]] <= E[i]:
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
    


l=[]
for i in range(5000):
	l.append(randint(0,100000))
E = [10, 15, 7, 19, 2, 5, 7, 16, 3, 9, 15, 0, 1, 15, 6, 11, 0, 14, 7, 9,18,29,9,3,57,92,4,182,34,58,2,3,472,502,382,594,90]
#E=l
#E=[10,80,70,3,50,40,98,4,0,3]
b = plus_grande_sequence_wikipedia(E)
print("E",E)
print("indice:",b)
print("\n\n")
print("valeurs:", [ E[i] for i in b ])
print("\ninformation process\n")
#print(process.memory_info().rss)
mem = process.memory_info()[0] / float(2 ** 20)
print(mem)
execution_time=time.time() - start_time
print("---Temps d'execution:  %s seconds ---" +str(execution_time))






