#! /bin/bash

(

	set -o xtrace

	g++ $1.cc /software/sb17498/pythia8223/lib/libpythia8.a -o $1.exe -I/software/sb17498/hepmcInstall/include -I/software/sb17498/pythia8223/include -O2 -ansi -pedantic -W -Wall -Wshadow -fPIC -Wl,-rpath,/software/sb17498/pythia8223/lib -ldl \
		-L/software/sb17498/hepmcInstall//lib -Wl,-rpath,/software/sb17498/hepmcInstall//lib -lHepMC\
		-I./ -I/software/sb17498/pythia8223/include -O2 -ansi -pedantic -W -Wall -Wshadow -fPIC -Wl,-rpath,/software/sb17498/pythia8223/lib -ldl \
		-pthread -std=c++1y -m64 -I/cvmfs/sft.cern.ch/lcg/releases/ROOT/6.08.06-c8fb4/x86_64-slc6-gcc49-opt/include \
		-L/cvmfs/sft.cern.ch/lcg/releases/ROOT/6.08.06-c8fb4/x86_64-slc6-gcc49-opt/lib -lGui -lCore -lRIO -lNet -lHist -lGraf -lGraf3d -lGpad -lTree -lRint -lPostscript -lMatrix -lPhysics -lMathCore -lThread -lMultiProc -pthread -lm -ldl -rdynamic

)