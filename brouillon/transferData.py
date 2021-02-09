# encoding: utf-8
def transferDataAlgo1():
	datafile=open("../data/data_algo1_time.dat","r")
	lines = datafile.readlines()
	count=0
	datafileTransfer=open("../data/data_algo1_time_all.dat","a")
	datafileTransfer.write(str(0)+";"+str(0))
	datafileTransfer.write("\n")
	for line in lines:
	    count += 1
	    data=line.strip()
	    dataTransfer=str(count)+";"+str(data)
	    datafileTransfer.write(dataTransfer)
	    datafileTransfer.write("\n")
	    
def transferDataAlgo2():
	datafile=open("../data/data_algo2_time.dat","r")
	lines = datafile.readlines()
	count=0
	datafileTransfer=open("../data/data_algo2_time_all.dat","a")
	datafileTransfer.write(str(0)+";"+str(0))
	datafileTransfer.write("\n")
	for line in lines:
	    count += 1
	    data=line.strip()
	    dataTransfer=str(count)+";"+str(data)
	    datafileTransfer.write(dataTransfer)
	    datafileTransfer.write("\n")
	    
def transferDataAlgo3():
	datafile=open("../data/data_algo3_time.dat","r")
	lines = datafile.readlines()
	count=0
	datafileTransfer=open("../data/data_algo3_time_all.dat","a")
	datafileTransfer.write(str(0)+";"+str(0))
	datafileTransfer.write("\n")
	for line in lines:
	    count += 1
	    data=line.strip()
	    dataTransfer=str(count)+";"+str(data)
	    datafileTransfer.write(dataTransfer)
	    datafileTransfer.write("\n")
	    
		
 

transferDataAlgo1()
transferDataAlgo2()
transferDataAlgo3()
