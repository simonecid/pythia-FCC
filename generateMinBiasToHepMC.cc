// main01.cc is a part of the PYTHIA event generator.
// Copyright (C) 2017 Torbjorn Sjostrand.
// PYTHIA is licenced under the GNU GPL version 2, see COPYING for details.
// Please respect the MCnet Guidelines, see GUIDELINES for details.

// This is a simple test program. It fits on one slide in a talk.
// It studies the charged multiplicity distribution at the LHC.

#include "Pythia8/Pythia.h"
#include "Pythia8Plugins/HepMC2.h" // Interface HepMC to Pythia8
#include "HepMC/GenEvent.h" // Generate HepMC event
#include "HepMC/IO_GenEvent.h" // IO stream for HepMC event
//#include "TFile.h"
//#include "TTree.h"
#include <string>

struct Particle {
  double px, py, pz, E, eta, phi;
};

//using namespace Pythia8;
int main(int argc, char * argv[]) {
  // Generator. Process selection. LHC initialization. Histogram.

  if (argc < 2) {
    std::cout << "Unique file index must be specified as a parameter." << std::endl;
    return -1;
  }

  Pythia8::Pythia pythia;
  HepMC::Pythia8ToHepMC ToHepMC;
  std::string hepMCFileName = "myhepmc_";
  hepMCFileName.append(argv[1]);
  hepMCFileName.append(".dat");
  HepMC::IO_GenEvent ascii_io(hepMCFileName.c_str(), std::ios::out);
  pythia.readFile("mymain00.cmnd");
  pythia.init();

  struct Particle resonanceToSave, decayProductsToSave[2];

  int nEvents = pythia.mode("Main:numberOfEvents");

  std::string rootFileName = "resonanceData_";
  rootFileName.append(argv[1]);
  rootFileName.append(".root");
  //TFile *myFile = TFile::Open(rootFileName.c_str(), "RECREATE");

  //TTree *tree = new TTree("resonanceDecays","Resonance two-particle decays");

  // Z0 Boson
  //tree->Branch("resonancePx",&resonanceToSave.px,"resonancePx/D");
  //tree->Branch("resonancePy",&resonanceToSave.py,"resonancePy/D");
  //tree->Branch("resonancePz",&resonanceToSave.pz,"resonancePz/D");
  //tree->Branch("resonanceE",&resonanceToSave.E,"resonanceE/D");
  //tree->Branch("resonanceEta",&resonanceToSave.eta,"resonanceEta/D");
  //tree->Branch("resonancePhi",&resonanceToSave.phi,"resonancePhi/D");
  
  // First decay product
  //tree->Branch("decay1Px",&decayProductsToSave[0].px,"decay1Px/D");
  //tree->Branch("decay1Py",&decayProductsToSave[0].py,"decay1Py/D");
  //tree->Branch("decay1Pz",&decayProductsToSave[0].pz,"decay1Pz/D");
  //tree->Branch("decay1E",&decayProductsToSave[0].E,"decay1E/D");
  //tree->Branch("decay1Eta",&decayProductsToSave[0].eta,"decay1Eta/D");
  //tree->Branch("decay1Phi",&decayProductsToSave[0].phi,"decay1Phi/D");

  // Second decay product  
  //tree->Branch("decay2Px",&decayProductsToSave[1].px,"decay2Px/D");
  //tree->Branch("decay2Py",&decayProductsToSave[1].py,"decay2Py/D");
  //tree->Branch("decay2Pz",&decayProductsToSave[1].pz,"decay2Pz/D");
  //tree->Branch("decay2E",&decayProductsToSave[1].E,"decay2E/D");
  //tree->Branch("decay2Eta",&decayProductsToSave[1].eta,"decay2Eta/D");
  //tree->Branch("decay2Phi",&decayProductsToSave[1].phi,"decay2Phi/D");

  // Begin event loop. Generate event. Skip if error. List first one.
  for (int iEvent = 0; iEvent < nEvents; ++iEvent) {
    if (!pythia.next()) continue;
    // Loop over particles in event. Find last Z0 copy. Fill its pT.
    //int iZ = 0;
    for (int i = 0; i < pythia.event.size(); ++i) {
      if (pythia.event[i].id() == 23) {
        const Pythia8::Particle * resonance = & pythia.event[i];
        //iZ = i;
        //std::cout << "Particle id: " << resonance -> id() << " with 4-p: " << resonance -> e() << " " << resonance -> px() << " " << resonance -> py() << " " << resonance -> pz() << std::endl;          
        const unsigned int numberOfDaughters = resonance -> daughterList().size();
        // We are interested only in two-particle decays
        if (numberOfDaughters != 2) continue;
        //Pythia8::Vec4 momentums[2];
        resonanceToSave.px = resonance -> px();
        resonanceToSave.py = resonance -> py();
        resonanceToSave.pz = resonance -> pz();
        resonanceToSave.E = resonance -> e();
        resonanceToSave.eta = resonance -> eta();
        resonanceToSave.phi = resonance -> phi();

        for (unsigned int x = 0; x < numberOfDaughters; x++) {
          int daughterIdx = resonance -> daughterList()[x];
          const Pythia8::Particle * resonanceProduct = & pythia.event[daughterIdx];
          //std::cout << "\t -> Particle id: " << resonanceProduct -> id() << " with 4-p: " << resonanceProduct -> e() << " " << resonanceProduct -> px() << " " << resonanceProduct -> py() << " " << resonanceProduct -> pz() << std::endl;          
          //momentums[x] = resonanceProduct -> p();

          decayProductsToSave[x].px = resonanceProduct -> px();
          decayProductsToSave[x].py = resonanceProduct -> py();
          decayProductsToSave[x].pz = resonanceProduct -> pz();
          decayProductsToSave[x].E = resonanceProduct -> e();
          decayProductsToSave[x].eta = resonanceProduct -> eta();
          decayProductsToSave[x].phi = resonanceProduct -> phi();

        }
        //double invariantMass = Pythia8::m(momentums[0], momentums[1]);
        //std::cout << "\t\t -> Mass is " << invariantMass << " GeV" << std::endl;

        //tree->Fill();
        
      }

    }    
    //std::cout << pythia.event[iZ].pT() << std::endl;
    // End of event loop. Statistics. Histogram. Done.

    HepMC::GenEvent* hepmcevt = new HepMC::GenEvent();
    ToHepMC.fill_next_event( pythia, hepmcevt );

    // Write the HepMC event to file. Done with it.
    ascii_io << hepmcevt;
    delete hepmcevt;

  }
  pythia.stat();

  //tree -> Write();
  //delete myFile;

  return 0;
  
}
