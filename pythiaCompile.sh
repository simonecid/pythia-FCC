#! /bin/bash

g++ $1 /software/sb17498/pythia8223/lib/libpythia8.a -o mymain00 -I/software/sb17498/hepmcInstall//include -I/software/sb17498/pythia8223/include -O2 -ansi -pedantic -W -Wall -Wshadow -fPIC -Wl,-rpath,/software/sb17498/pythia8223/lib -ldl \
	 -L/software/sb17498/hepmcInstall//lib -Wl,-rpath,/software/sb17498/hepmcInstall//lib -lHepMC\
	 -I./ -I/software/sb17498/pythia8223/include -O2 -ansi -pedantic -W -Wall -Wshadow -fPIC -Wl,-rpath,/software/sb17498/pythia8223/lib -ldl 
	 #-pthread -m32 -I/software/root/v5.34.25/include \
	 #-Wl,-rpath,./ -L/software/root/v5.34.25/lib -lCore -lCint -lRIO -lNet -lHist -lGraf -lGraf3d -lGpad -lTree -lRint -lPostscript -lMatrix -lPhysics -lMathCore -lThread -lGui -pthread -lm -ldl -rdynamic
