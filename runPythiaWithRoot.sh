#!/bin/bash

source /cvmfs/sft.cern.ch/lcg/contrib/gcc/4.9/x86_64-slc6/setup.sh
source /cvmfs/sft.cern.ch/lcg/releases/ROOT/6.08.06-c8fb4/x86_64-slc6-gcc49-opt/bin/thisroot.sh
/software/sb17498/pythia8223/pythia-FCC/generateHiggs_WWZZ_leptons_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_H_WW_enuenu.cmnd -o ff_H_WW_enuenu
/software/sb17498/pythia8223/pythia-FCC/generateHiggs_WWZZ_leptons_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_H_WW_munumunu.cmnd -o ff_H_WW_munumunu
/software/sb17498/pythia8223/pythia-FCC/generateHiggs_WWZZ_leptons_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_H_ZZ_eeee.cmnd -o ff_H_ZZ_eeee
/software/sb17498/pythia8223/pythia-FCC/generateHiggs_WWZZ_leptons_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_H_ZZ_mumumumu.cmnd -o ff_H_ZZ_mumumumu
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToTwoParticle_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_W_enu.cmnd -o ff_W_enu_14TeV
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToTwoParticle_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_W_munu.cmnd -o ff_W_munu_14TeV
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToTwoParticle_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_Z_ee.cmnd -o ff_Z_ee_14TeV
/software/sb17498/pythia8223/pythia-FCC/generateResonanceToTwoParticle_HepMC_ROOT.exe -c /software/sb17498/pythia8223/pythia-FCC/ff_Z_mumu.cmnd -o ff_Z_mumu_14TeV