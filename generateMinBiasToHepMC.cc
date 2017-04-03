#include "Pythia8/Pythia.h"
#include "Pythia8Plugins/HepMC2.h" // Interface HepMC to Pythia8
#include "HepMC/GenEvent.h" // Generate HepMC event
#include "HepMC/IO_GenEvent.h" // IO stream for HepMC event
//#include "TFile.h"
//#include "TTree.h"
#include <string>
#include <unistd.h> //getopt
#include <sstream>

//using namespace Pythia8;
int main(int argc, char * argv[]) {
  // Generator. Process selection. LHC initialization. Histogram.

  // -c -> command file
  // -n -> .dat file name suffix for unique output identification

  std::istringstream inputHandler;

  std::string cmndFileName;
  std::string fileSuffix;

  int c;

  while ((c = getopt (argc, argv, "cn")) != -1)
  switch (c)
  {
    case 'c':
      std::cout << optind << "\t" << argv[optind] << std::endl;
      inputHandler >> cmndFileName;
      inputHandler.str(argv[optind]);
      cmndFileName = argv[optind];
      break;
    
    case 'n':
      std::cout << optind << "\t" << argv[optind] << std::endl;
      inputHandler.str(argv[optind]);
      fileSuffix = argv[optind];
      break;

    default:
      abort ();
  }

  Pythia8::Pythia pythia;
  HepMC::Pythia8ToHepMC ToHepMC;
  std::string hepMCFileName = "minBiasEvents/minBias_";
  hepMCFileName.append(fileSuffix);
  hepMCFileName.append(".dat");
  HepMC::IO_GenEvent ascii_io(hepMCFileName.c_str(), std::ios::out);
  pythia.readFile(cmndFileName.c_str());
  pythia.init();

  int nEvents = pythia.mode("Main:numberOfEvents");

  // Begin event loop. Generate event. Skip if error. List first one.
  for (int iEvent = 0; iEvent < nEvents; ++iEvent) {
    if (!pythia.next()) continue;

    HepMC::GenEvent* hepmcevt = new HepMC::GenEvent();
    ToHepMC.fill_next_event( pythia, hepmcevt );

    // Write the HepMC event to file. Done with it.
    ascii_io << hepmcevt;
    delete hepmcevt;

  }
  pythia.stat();

  return 0;
  
}
