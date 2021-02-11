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

set yrange [0:1.2]
set xrange [0:51]

#set title "L1 cache"
     
set xlabel "lancements"
set ylabel "temps execution"
set datafile separator ";"
set title "graphe histogrammes du temps d'éxecution pour les lancements"
plot "data/data_algo1_time_all.dat" u 2:xtic(1) t "algo1 (recursive)", \
     "data/data_algo2_time_all.dat" u 2:xtic(1) t "algo2 (non recursive)", \
     "data/data_algo3_time_all.dat" u 2:xtic(1) t "algo3 (algo wikipedia)"

set title "graphe courbes du temps d'éxecution pour les lancements"  
plot "data/data_algo1_time_all.dat" u 2:xtic(1) t "algo1 (recursive)" with linespoints, \
     "data/data_algo2_time_all.dat" u 2:xtic(1) t "algo2 (non recursive)" with linespoints , \
     "data/data_algo3_time_all.dat" u 2:xtic(1) t "algo3 (algo wikipedia)" with linespoints
     
set yrange [0:25]
set xrange [0:51]
set xlabel "lancements"
set ylabel "utilisation de la memoire (MB)"
set title "graphe histogrammes d'utilisation de la mémoire en MB pour les lancements"
plot "data/data_algo1_memory_all.dat" u 2:xtic(1) t "algo1 (recursive)", \
     "data/data_algo2_memory_all.dat" u 2:xtic(1) t "algo2 (non recursive)", \
     "data/data_algo3_memory_all.dat" u 2:xtic(1) t "algo3 (algo wikipedia)"
     
 set title "graphe courbes du temps d'éxecution pour les lancements"  
plot "data/data_algo1_memory_all.dat" u 2:xtic(1) t "algo1 (recursive)" with linespoints, \
     "data/data_algo2_memory_all.dat" u 2:xtic(1) t "algo2 (non recursive)" with linespoints , \
     "data/data_algo3_memory_all.dat" u 2:xtic(1) t "algo3 (algo wikipedia)" with linespoints

unset multiplot
