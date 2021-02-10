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

set yrange [0:0.1]
set xrange [0:51]

#set title "L1 cache"
     
set xlabel "lancements"
set ylabel "temps execution"
set datafile separator ";"
plot "data/data_algo1_time_all.dat" u 2:xtic(1) t "algo1", \
     "data/data_algo2_time_all.dat" u 2:xtic(1) t "algo2", \
     "data/data_algo3_time_all.dat" u 2:xtic(1) t "algo3"
     
plot "data/data_algo1_time_all.dat" u 2:xtic(1) t "algo1" with linespoints, \
     "data/data_algo2_time_all.dat" u 2:xtic(1) t "algo2" with linespoints , \
     "data/data_algo3_time_all.dat" u 2:xtic(1) t "algo3" with linespoints

unset multiplot
