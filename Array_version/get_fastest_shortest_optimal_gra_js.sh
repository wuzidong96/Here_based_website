#usage ./get_fastest_shortest_optimal_gra_js.sh src des T
src=$1
des=$2
T=$3
instance=$1_$2_$3
#echo $instance
./convert_gra_js.sh result/T800/path/path_fastest_${instance}.gra > trash_fastest
./convert_gra_js.sh result/T800/path/path_shortest_${instance}.gra > trash_shortest
./convert_gra_js.sh result/T800/path/path_opt_${instance}.gra > trash_optimal

cat show_path_part_1.html \
    trash_fastest \
    show_path_part_2.html \
    trash_shortest \
    show_path_part_3.html \
    trash_optimal \
    show_path_part_4.html > html/show_path_${instance}.html
