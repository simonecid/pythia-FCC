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
  // -o -> path of output file
  // -n -> number of events to generate

  std::string cmndFileName;
  std::string outputFilename;
  int numberOfEvents = -1;
  std::string setSeedCommand = "Random:seed  = ";


  int c;
  while ((c = getopt (argc, argv, "cnos")) != -1)
  switch (c)
  {
    case 'c': {
      cmndFileName = argv[optind];
      break;
    }

    case 'o': {
      outputFilename = argv[optind];
      break;
    }

    case 'n': {
      std::string numberOfEvents_str = argv[optind];
      std::istringstream iss;
      iss.str(numberOfEvents_str);
      iss >> numberOfEvents;
      break;
    }

    case 's': {
      std::string seed = argv[optind];
      std::cout << "Seed has been set to " << seed << std::endl;
      setSeedCommand.append(seed);
      break;
    }
    default:
      abort ();
  }

  Pythia8::Pythia pythia;
  HepMC::Pythia8ToHepMC ToHepMC;
  HepMC::IO_GenEvent ascii_io(outputFilename.c_str(), std::ios::out);
  pythia.readFile(cmndFileName.c_str());
  pythia.readString("Random:setSeed = on");
  pythia.readString(setSeedCommand);
  pythia.init();

  if (numberOfEvents <= 0) numberOfEvents = pythia.mode("Main:numberOfEvents");

  // Begin event loop. Generate event. Skip if error. List first one.
  for (int iEvent = 0; iEvent < numberOfEvents; ++iEvent) {
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
