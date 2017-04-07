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

#include "PythiaUtils.h"

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
  // -r -> higgsId (absolute value will be taken)
  // -n -> number of events to generate (facultative)

  std::string cmndFileName;
  std::string outputFileName;
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

  struct Particle higgsToSave, ewBosonsToSave[2],leptonProductsToSave[4];

  if (nEvents == 0) nEvents = pythia.mode("Main:numberOfEvents");

  std::string rootFileName = outputFileName;
  rootFileName.append(".root");
  TFile *myFile = TFile::Open(rootFileName.c_str(), "RECREATE");

  TTree *tree = new TTree("higgsDecays","Higgs boson two-particle decays");

  // higgs
  tree -> Branch("higgsPx",&higgsToSave.px,"higgsPx/D");
  tree -> Branch("higgsPy",&higgsToSave.py,"higgsPy/D");
  tree -> Branch("higgsPz",&higgsToSave.pz,"higgsPz/D");
  tree -> Branch("higgsE",&higgsToSave.E,"higgsE/D");
  tree -> Branch("higgsEta",&higgsToSave.eta,"higgsEta/D");
  tree -> Branch("higgsPhi",&higgsToSave.phi,"higgsPhi/D");
  tree -> Branch("higgsPDGID",&higgsToSave.pdgid,"higgsPDGID/I");

  // EW boson 1
  tree -> Branch("ewBoson1Px",&ewBosonsToSave[0].px,"ewBoson1Px/D");
  tree -> Branch("ewBoson1Py",&ewBosonsToSave[0].py,"ewBoson1Py/D");
  tree -> Branch("ewBoson1Pz",&ewBosonsToSave[0].pz,"ewBoson1Pz/D");
  tree -> Branch("ewBoson1E",&ewBosonsToSave[0].E,"ewBoson1E/D");
  tree -> Branch("ewBoson1Eta",&ewBosonsToSave[0].eta,"ewBoson1Eta/D");
  tree -> Branch("ewBoson1Phi",&ewBosonsToSave[0].phi,"ewBoson1Phi/D");
  tree -> Branch("ewBoson1PDGID",&ewBosonsToSave[0].pdgid,"ewBoson1PDGID/I");
  
  // EW boson 2
  tree -> Branch("ewBoson2Px",&ewBosonsToSave[1].px,"ewBoson2Px/D");
  tree -> Branch("ewBoson2Py",&ewBosonsToSave[1].py,"ewBoson2Py/D");
  tree -> Branch("ewBoson2Pz",&ewBosonsToSave[1].pz,"ewBoson2Pz/D");
  tree -> Branch("ewBoson2E",&ewBosonsToSave[1].E,"ewBoson2E/D");
  tree -> Branch("ewBoson2Eta",&ewBosonsToSave[1].eta,"ewBoson2Eta/D");
  tree -> Branch("ewBoson2Phi",&ewBosonsToSave[1].phi,"ewBoson2Phi/D");
  tree -> Branch("ewBoson2PDGID",&ewBosonsToSave[1].pdgid,"ewBoson2PDGID/I");
  
  // First lepton product
  tree -> Branch("lepton1Px",&leptonProductsToSave[0].px,"lepton1Px/D");
  tree -> Branch("lepton1Py",&leptonProductsToSave[0].py,"lepton1Py/D");
  tree -> Branch("lepton1Pz",&leptonProductsToSave[0].pz,"lepton1Pz/D");
  tree -> Branch("lepton1E",&leptonProductsToSave[0].E,"lepton1E/D");
  tree -> Branch("lepton1Eta",&leptonProductsToSave[0].eta,"lepton1Eta/D");
  tree -> Branch("lepton1Phi",&leptonProductsToSave[0].phi,"lepton1Phi/D");
  tree -> Branch("lepton1PDGID",&leptonProductsToSave[0].pdgid,"lepton1PDGID/I");

  // Second lepton product  
  tree -> Branch("lepton2Px",&leptonProductsToSave[1].px,"lepton2Px/D");
  tree -> Branch("lepton2Py",&leptonProductsToSave[1].py,"lepton2Py/D");
  tree -> Branch("lepton2Pz",&leptonProductsToSave[1].pz,"lepton2Pz/D");
  tree -> Branch("lepton2E",&leptonProductsToSave[1].E,"lepton2E/D");
  tree -> Branch("lepton2Eta",&leptonProductsToSave[1].eta,"lepton2Eta/D");
  tree -> Branch("lepton2Phi",&leptonProductsToSave[1].phi,"lepton2Phi/D");
  tree -> Branch("lepton2PDGID",&leptonProductsToSave[1].pdgid,"lepton2PDGID/I");

  // Third lepton product
  tree -> Branch("lepton3Px",&leptonProductsToSave[2].px,"lepton3Px/D");
  tree -> Branch("lepton3Py",&leptonProductsToSave[2].py,"lepton3Py/D");
  tree -> Branch("lepton3Pz",&leptonProductsToSave[2].pz,"lepton3Pz/D");
  tree -> Branch("lepton3E",&leptonProductsToSave[2].E,"lepton3E/D");
  tree -> Branch("lepton3Eta",&leptonProductsToSave[2].eta,"lepton3Eta/D");
  tree -> Branch("lepton3Phi",&leptonProductsToSave[2].phi,"lepton3Phi/D");
  tree -> Branch("lepton3PDGID",&leptonProductsToSave[2].pdgid,"lepton3PDGID/I");

  // Fourth lepton product  
  tree -> Branch("lepton4Px",&leptonProductsToSave[3].px,"lepton4Px/D");
  tree -> Branch("lepton4Py",&leptonProductsToSave[3].py,"lepton4Py/D");
  tree -> Branch("lepton4Pz",&leptonProductsToSave[3].pz,"lepton4Pz/D");
  tree -> Branch("lepton4E",&leptonProductsToSave[3].E,"lepton4E/D");
  tree -> Branch("lepton4Eta",&leptonProductsToSave[3].eta,"lepton4Eta/D");
  tree -> Branch("lepton4Phi",&leptonProductsToSave[3].phi,"lepton4Phi/D");
  tree -> Branch("lepton4PDGID",&leptonProductsToSave[3].pdgid,"lepton4PDGID/I");

  // Begin event loop. Generate event. Skip if error. List first one.
  for (int iEvent = 0; iEvent < nEvents; ++iEvent) 
  {
    if (!pythia.next()) continue;
    // Loop over particles in event. Find decaying H0.
    for (int i = 0; i < pythia.event.size(); ++i) 
    {
      if (abs(pythia.event[i].id()) == 25) 
      {
        const Pythia8::Particle * higgs = & pythia.event[i];
        //iZ = i;
        //std::cout << "Particle id: " << higgs -> id() << " with 4-p: " << higgs -> e() << " " << higgs -> px() << " " << higgs -> py() << " " << higgs -> pz() << std::endl;          
        const unsigned int numberOfDaughters = higgs -> daughterList().size();
        // We are interested only in the decays in 2 EW bosons
        if (numberOfDaughters != 2) continue;
        
        // Storing Higgs boson data
        higgsToSave.px = higgs -> px();
        higgsToSave.py = higgs -> py();
        higgsToSave.pz = higgs -> pz();
        higgsToSave.E = higgs -> e();
        higgsToSave.eta = higgs -> eta();
        higgsToSave.phi = higgs -> phi();
        higgsToSave.pdgid = higgs -> id();

        //Storing EW bosons data
        for (unsigned int x = 0; x < numberOfDaughters; x++) 
        {
          int daughterIdx = higgs -> daughterList()[x];
          const Pythia8::Particle * ewBoson = PythiaUtils::findDecayNode(& pythia.event, & pythia.event[daughterIdx]);
          ewBosonsToSave[x].px = ewBoson -> px();
          ewBosonsToSave[x].py = ewBoson -> py();
          ewBosonsToSave[x].pz = ewBoson -> pz();
          ewBosonsToSave[x].E = ewBoson -> e();
          ewBosonsToSave[x].eta = ewBoson -> eta();
          ewBosonsToSave[x].phi = ewBoson -> phi();
          ewBosonsToSave[x].pdgid = ewBoson -> id();

          //Saving the lepton data
          
          const unsigned int numberOfEWBosonDecayProducts = ewBoson -> daughterList().size();

          if (numberOfEWBosonDecayProducts != 2)
          {
            printf ("SHIT IS HAPPENING, BEWARE! \n");
          }

          for (unsigned int y = 0; y < numberOfEWBosonDecayProducts; y++)
          {
            // First W/Z produces lepton 0 & 1
            // Second W/Z produces lepton 2 & 3
            const unsigned int leptonSaveIdx = x * 2 + y;
            int leptonIdx = ewBoson -> daughterList()[y];
            const Pythia8::Particle* lepton = & pythia.event[leptonIdx];

            leptonProductsToSave[leptonSaveIdx].px = lepton -> px();
            leptonProductsToSave[leptonSaveIdx].py = lepton -> py();
            leptonProductsToSave[leptonSaveIdx].pz = lepton -> pz();
            leptonProductsToSave[leptonSaveIdx].E = lepton -> e();
            leptonProductsToSave[leptonSaveIdx].eta = lepton -> eta();
            leptonProductsToSave[leptonSaveIdx].phi = lepton -> phi();
            leptonProductsToSave[leptonSaveIdx].pdgid = lepton -> id();
            
          }

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
