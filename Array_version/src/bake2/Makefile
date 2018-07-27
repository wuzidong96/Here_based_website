SNAPROOT = ~/intern/PASO_CCH/PASO_CCH/Snap-4.0
GEOROOT = ~/intern/PASO_CCH/PASO_CCH/GeographicLib-1.49/src
KITROOT = ~/intern/PASO_CCH/PASO_CCH/RoutingKit

CGEO = $(GEOROOT)/../include
GEOLIB = $(GEOROOT)
KITINCLUDE = $(KITROOT)/include
KITLIB = $(KITROOT)/lib

GLIB = glib-core
SNAP = snap-core
GLIBADV = glib-adv
SNAPADV = snap-adv
SNAPEXP = snap-exp

CGLIB = $(SNAPROOT)/$(GLIB)
CSNAP = $(SNAPROOT)/$(SNAP)

#copied from SNAP Makefile.config
CC = g++
CXXFLAGS += -std=c++11 -Wall
CXXFLAGS += -O3 -DNDEBUG
# turn on for crash debugging, get symbols with <prog> 2>&1 | c++filt
#CXXFLAGS += -g -rdynamic
CXXOPENMP = -fopenmp
LDFLAGS += $(CXXOPENMP)
# LIBS += -lrt

#for  geographic
LIBS += -lGeographic
LIBS += -lroutingkit

INC +=-I$(CSNAP)
INC +=-I$(CGLIB)
INC +=-I$(CGEO)
INC +=-I$(KITINCLUDE)
LIBINC +=-L$(GEOLIB) 
LIBINC +=-L$(KITLIB)

SRCS = \
PASONodeData.cpp\
PASOEdgeData.cpp\
PASOSolution.cpp\
PASOUtil.cpp\
main.cpp

OBJS = $(SRCS:.cpp=.o)

#add option for addressing cxx11
ADD = -D_GLIBCXX_USE_CXX11_ABI=0
	
## Main application file
TAR = \
	../main

all: $(TAR)

# COMPILE
$(TAR): $(OBJS)
	$(CC) $(CXXFLAGS) $(ADD) $(INC) $(LIBINC) $(LDFLAGS) $(CSNAP)/Snap.o $(OBJS) $(LIBS) -o $@ 

%.o: %.cpp
	$(CC) $(CXXFLAGS) $(INC) $(LIBINC) $(LDFLAGS) $(LIBS) -o $@ -c $<

clean:
	rm -f *.o $(TAR)

