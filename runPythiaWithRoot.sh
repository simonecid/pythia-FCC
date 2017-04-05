#!/bin/bash

source /cvmfs/sft.cern.ch/lcg/contrib/gcc/4.9/x86_64-slc6/setup.sh
source /cvmfs/sft.cern.ch/lcg/releases/ROOT/6.08.06-c8fb4/x86_64-slc6-gcc49-opt/bin/thisroot.sh
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToHepMCAndROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ffZee.cmnd -o ffZee_1000evts
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToHepMCAndROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ffZmumu.cmnd -o ffZmumu_1000evts
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToHepMCAndROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ffZtautau.cmnd -o ffZtautau_1000evts