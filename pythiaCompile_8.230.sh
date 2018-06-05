
(

	set -o xtrace

  g++ $1.cc /cvmfs/fcc.cern.ch/testing/lcgview/LCG_92/x86_64-slc6-gcc62-opt/lib/libpythia8.a -o $1.exe -I/cvmfs/fcc.cern.ch/testing/lcgview/LCG_92/x86_64-slc6-gcc62-opt/include -I/cvmfs/fcc.cern.ch/testing/lcgview/LCG_92/x86_64-slc6-gcc62-opt/include -O2 -ansi -pedantic -W -Wall -Wshadow -fPIC -Wl,-rpath,/cvmfs/fcc.cern.ch/testing/lcgview/LCG_92/x86_64-slc6-gcc62-opt/lib -ldl \
      -L/cvmfs/fcc.cern.ch/testing/lcgview/LCG_92/x86_64-slc6-gcc62-opt/lib/ -Wl,-rpath,/cvmfs/fcc.cern.ch/testing/lcgview/LCG_92/x86_64-slc6-gcc62-opt/lib/ -lHepMC\
      -I./ -I/cvmfs/fcc.cern.ch/testing/lcgview/LCG_92/x86_64-slc6-gcc62-opt/include -O2 -ansi -pedantic -W -Wall -Wshadow -fPIC -Wl,-rpath,/cvmfs/fcc.cern.ch/testing/lcgview/LCG_92/x86_64-slc6-gcc62-opt/lib -ldl \
      -pthread -std=c++1y -m64 -I/cvmfs/sft.cern.ch/lcg/releases/ROOT/6.08.06-c8fb4/x86_64-slc6-gcc49-opt/include \
      -L/cvmfs/sft.cern.ch/lcg/releases/ROOT/6.08.06-c8fb4/x86_64-slc6-gcc49-opt/lib -lGui -lCore -lRIO -lNet -lHist -lGraf -lGraf3d -lGpad -lTree -lRint -lPostscript -lMatrix -lPhysics -lMathCore -lThread -lMultiProc -pthread -lm -ldl -rdynamic
      
)