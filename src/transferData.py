# encoding: utf-8
def transferDataAlgoData(entree,sortie):
	datafile=open(entree,"r")
	lines = datafile.readlines()
	count=0
	datafileTransfer=open(sortie,"a")
	datafileTransfer.write(str(0)+";"+str(0))
	datafileTransfer.write("\n")
	for line in lines:
	    count += 1
	    data=line.strip()
	    dataTransfer=str(count)+";"+str(data)
	    datafileTransfer.write(dataTransfer)
	    datafileTransfer.write("\n")

	    	
 
"""
Temps
"""
transferDataAlgoData("../data/data_algo1_time.dat","../data/data_algo1_time_all.dat")
transferDataAlgoData("../data/data_algo2_time.dat","../data/data_algo2_time_all.dat")
transferDataAlgoData("../data/data_algo3_time.dat","../data/data_algo3_time_all.dat")

"""
Memoire
"""
transferDataAlgoData("../data/data_algo1_memory.dat","../data/data_algo1_memory_all.dat")
transferDataAlgoData("../data/data_algo2_memory.dat","../data/data_algo2_memory_all.dat")
transferDataAlgoData("../data/data_algo3_memory.dat","../data/data_algo3_memory_all.dat")
