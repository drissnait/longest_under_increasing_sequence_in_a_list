
set term png size 1900,1000 enhanced font "Terminal,10"

set grid

set auto x

set key left top

#set title "Intel(R) Core(TM) i5-8250U bandwidth (in GiB/s) for a Load benchmark on a single array"

#set xlabel "Benchmark variants"
set ylabel "Bandwidth in GiB/s (higher is better)
set style data histogram
set style fill solid border -1
set boxwidth 0.9
set xtic rotate by -45 scale 0
set multiplot layout 2, 2 rowsfirst


set datafile separator ";"
set yrange [0:0.2]
set xrange [0:11]
set title "courbe du temps d'éxecution pour les lancements de la version récursive"
plot "data/data_algo1_time_all.dat" u 2:xtic(1) t "algo recursif" with linespoints

set yrange [0:10]
set xrange [0:11]
set xlabel "lancements"
set ylabel "temps execution"
set title "courbe du temps d'éxecution pour les lancements de la version itérative"
plot "data/data_algo2_time_all.dat" u 2:xtic(1) t "algo iteratif" with linespoints

set yrange [0:25]
set xrange [0:11]
set title "courbe d'espace memoire pour les lancements"
plot "data/data_algo1_memory_all.dat" u 2:xtic(1) t "algo recursif" with linespoints, \
	"data/data_algo2_memory_all.dat" u 2:xtic(1) t "algo iteratif" with linespoints




