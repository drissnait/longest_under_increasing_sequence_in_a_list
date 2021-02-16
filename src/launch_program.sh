#!/bin/bash
rm ../data/data_algo1_time.dat
rm ../data/data_algo2_time.dat
rm ../data/data_algo3_time.dat

rm ../data/data_algo1_memory.dat
rm ../data/data_algo2_memory.dat
rm ../data/data_algo3_memory.dat

rm ../resultat_test/resultat_test_algo1.dat
rm ../resultat_test/resultat_test_algo2.dat
rm ../resultat_test/resultat_test_algo3.dat
 
for i in {1..10}
do
   python3 algo1.py
   python3 algo2.py
   python3 algo3.py
done
rm ../data/data_algo1_time_all.dat
rm ../data/data_algo2_time_all.dat
rm ../data/data_algo3_time_all.dat

rm ../data/data_algo1_memory_all.dat
rm ../data/data_algo2_memory_all.dat
rm ../data/data_algo3_memory_all.dat

python3 transferData.py
rm ../data/data_algo1_time.dat
rm ../data/data_algo2_time.dat
rm ../data/data_algo3_time.dat

rm ../data/data_algo1_memory.dat
rm ../data/data_algo2_memory.dat
rm ../data/data_algo3_memory.dat
