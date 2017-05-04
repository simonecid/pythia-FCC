#!/bin/bash

source /cvmfs/sft.cern.ch/lcg/contrib/gcc/4.9/x86_64-slc6/setup.sh
source /cvmfs/sft.cern.ch/lcg/releases/ROOT/6.08.06-c8fb4/x86_64-slc6-gcc49-opt/bin/thisroot.sh
/software/sb17498/pythia8223/pythia-FCC/generateHiggs_WWZZ_leptons_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_H_WW_enuenu_100TeV.cmnd -o ff_H_WW_enuenu_1000events_100TeV -n 1000
/software/sb17498/pythia8223/pythia-FCC/generateHiggs_WWZZ_leptons_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_H_WW_munumunu_100TeV.cmnd -o ff_H_WW_munumunu_1000events_100TeV -n 1000
/software/sb17498/pythia8223/pythia-FCC/generateHiggs_WWZZ_leptons_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_H_ZZ_eeee_100TeV.cmnd -o ff_H_ZZ_eeee_1000events_100TeV -n 1000
/software/sb17498/pythia8223/pythia-FCC/generateHiggs_WWZZ_leptons_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_H_ZZ_mumumumu_100TeV.cmnd -o ff_H_ZZ_mumumumu_1000events_100TeV -n 1000
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToTwoParticle_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_W_enu_100TeV.cmnd -o ff_W_enu_1000events_100TeV -n 1000
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToTwoParticle_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_W_munu_100TeV.cmnd -o ff_W_munu_1000events_100TeV -n 1000
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToTwoParticle_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_Z_ee_100TeV.cmnd -o ff_Z_ee_1000events_100TeV -n 1000
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToTwoParticle_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_Z_mumu_100TeV.cmnd -o ff_Z_mumu_1000events_100TeV -n 1000