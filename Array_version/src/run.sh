# export CPLUS_INCLUDE_PATH=~/intern/PASO_CCH/PASO_CCH/Snap-4.0
# export CPLUS_INCLUDE_PATH=~/intern/PASO_CCH/PASO_CCH/GeographicLib-1.49/src
# export CPLUS_INCLUDE_PATH=~/intern/PASO_CCH/PASO_CCH/RoutingKit

# g++ -std=c++11 -c PASONodeData.cpp  -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/snap-core -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/glib-core  -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/glib-core
# -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/glib-core -I ~/intern/PASO_CCH/PASO_CCH/GeographicLib-1.49/src -I ~/intern/PASO_CCH/PASO_CCH/RoutingKit/include
g++ -std=c++11 -c PASOEdgeData.cpp  -o PASOEdgeData.o -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/snap-core -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/glib-core -I ~/intern/PASO_CCH/PASO_CCH/GeographicLib-1.49/include ~/intern/PASO_CCH/PASO_CCH/GeographicLib-1.49/include -I ~/intern/PASO_CCH/PASO_CCH/RoutingKit/include
g++ -std=c++11 -c PASOSolution.cpp  -o PASOSolution.o -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/snap-core -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/glib-core -I ~/intern/PASO_CCH/PASO_CCH/GeographicLib-1.49/include -I ~/intern/PASO_CCH/PASO_CCH/RoutingKit/include
g++ -std=c++11 -c PASOUtil.cpp  -o PASOUtil.o -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/snap-core -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/glib-core -I ~/intern/PASO_CCH/PASO_CCH/GeographicLib-1.49/include -I ~/intern/PASO_CCH/PASO_CCH/RoutingKit/include
g++ -std=c++11 -c main.cpp  -o main.o -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/snap-core -I ~/intern/PASO_CCH/PASO_CCH/Snap-4.0/glib-core -I ~/intern/PASO_CCH/PASO_CCH/GeographicLib-1.49/include -I ~/intern/PASO_CCH/PASO_CCH/RoutingKit/include

