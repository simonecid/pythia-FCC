#include "Pythia8/Pythia.h"
#include "Pythia8Plugins/HepMC2.h" // Interface HepMC to Pythia8
#include "HepMC/GenEvent.h" // Generate HepMC event
#include "HepMC/IO_GenEvent.h" // IO stream for HepMC event
#include "TFile.h"
#include "TTree.h"
#include <string>
#include <unistd.h> //getopt
#include <sstream> 
#include <cstdlib>

struct Particle
{
  double px, py, pz, E, eta, phi;
  int pdgid;
};

//using namespace Pythia8;
int main(int argc, char * argv[]) 
{
  // Generator. Process selection. LHC initialization. Histogram.

  // -c -> command file
  // -o -> ID for unique output identification
  // -r -> resonanceId (absolute value will be taken)
  // -n -> number of events to generate (facultative)

  std::string cmndFileName;
  std::string outputFileName;
  int resonancePDGID;
  int nEvents = 0;

  int c;

  while ((c = getopt (argc, argv, "corn")) != -1)
  switch (c)
  {
    case 'c':      
    {
      cmndFileName = argv[optind];
      break;
    }
    case 'o':
    {
      outputFileName = argv[optind];
      break;
    }
    case 'r':
    {
      std::string resonancePDGID_str;
      resonancePDGID_str = argv[optind];
      std::istringstream converter;
      converter.str(resonancePDGID_str);
      converter >> resonancePDGID;
      break;
    }
    case 'n':
    {
      std::string nEvents_str;
      nEvents_str = argv[optind];
      std::istringstream converter;
      converter.str(nEvents_str);
      converter >> nEvents;
      break;
    } 
    default:
    {
      abort ();
    }
  }

  Pythia8::Pythia pythia;
  HepMC::Pythia8ToHepMC ToHepMC;
  std::string hepMCFileName = outputFileName;
  hepMCFileName.append(".dat");
  HepMC::IO_GenEvent ascii_io(hepMCFileName.c_str(), std::ios::out);
  pythia.readFile(cmndFileName.c_str());
  pythia.init();

  struct Particle resonanceToSave, decayProductsToSave[2];

  if (nEvents == 0) nEvents = pythia.mode("Main:numberOfEvents");

  std::string rootFileName = outputFileName;
  rootFileName.append(".root");
  TFile *myFile = TFile::Open(rootFileName.c_str(), "RECREATE");

  TTree *tree = new TTree("resonanceDecays","Resonance two-particle decays");

  // Resonance
  tree -> Branch("resonancePx",&resonanceToSave.px,"resonancePx/D");
  tree -> Branch("resonancePy",&resonanceToSave.py,"resonancePy/D");
  tree -> Branch("resonancePz",&resonanceToSave.pz,"resonancePz/D");
  tree -> Branch("resonanceE",&resonanceToSave.E,"resonanceE/D");
  tree -> Branch("resonanceEta",&resonanceToSave.eta,"resonanceEta/D");
  tree -> Branch("resonancePhi",&resonanceToSave.phi,"resonancePhi/D");
  tree -> Branch("resonancePDGID",&resonanceToSave.pdgid,"resonancePDGID/I");
  
  // First decay product
  tree -> Branch("decay1Px",&decayProductsToSave[0].px,"decay1Px/D");
  tree -> Branch("decay1Py",&decayProductsToSave[0].py,"decay1Py/D");
  tree -> Branch("decay1Pz",&decayProductsToSave[0].pz,"decay1Pz/D");
  tree -> Branch("decay1E",&decayProductsToSave[0].E,"decay1E/D");
  tree -> Branch("decay1Eta",&decayProductsToSave[0].eta,"decay1Eta/D");
  tree -> Branch("decay1Phi",&decayProductsToSave[0].phi,"decay1Phi/D");
  tree -> Branch("decay1PDGID",&decayProductsToSave[0].pdgid,"decay1PDGID/I");

  // Second decay product  
  tree -> Branch("decay2Px",&decayProductsToSave[1].px,"decay2Px/D");
  tree -> Branch("decay2Py",&decayProductsToSave[1].py,"decay2Py/D");
  tree -> Branch("decay2Pz",&decayProductsToSave[1].pz,"decay2Pz/D");
  tree -> Branch("decay2E",&decayProductsToSave[1].E,"decay2E/D");
  tree -> Branch("decay2Eta",&decayProductsToSave[1].eta,"decay2Eta/D");
  tree -> Branch("decay2Phi",&decayProductsToSave[1].phi,"decay2Phi/D");
  tree -> Branch("decay2PDGID",&decayProductsToSave[1].pdgid,"decay2PDGID/I");

  // Begin event loop. Generate event. Skip if error. List first one.
  for (int iEvent = 0; iEvent < nEvents; ++iEvent) 
  {
    if (!pythia.next()) continue;
    // Loop over particles in event. Find last Z0 copy. Fill its pT.
    //int iZ = 0;
    for (int i = 0; i < pythia.event.size(); ++i) 
    {
      if (abs(pythia.event[i].id()) == abs(resonancePDGID)) 
      {
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
        resonanceToSave.pdgid = resonance -> id();

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
          decayProductsToSave[x].pdgid = resonanceProduct -> id();

        }
        //double invariantMass = Pythia8::m(momentums[0], momentums[1]);
        //std::cout << "\t\t -> Mass is " << invariantMass << " GeV" << std::endl;

        tree -> Fill();
        
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

  tree -> Write();
  delete myFile;

  return 0;
  
}
