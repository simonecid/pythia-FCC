#include "Pythia8/Pythia.h"

namespace PythiaUtils{

  /**
    Browse through the particle list of a Pythia event to find the Pythia8::Particle object which decays 
    and does not the propagated.
    Since I like when stuff blows up in my hands I use recursion, w8ing 4 a stack overflow <3.
  */
  const Pythia8::Particle* findDecayNode(const Pythia8::Event* aEvent, const Pythia8::Particle* aUnstableParticle)
  {
    const unsigned int numberOfDaughters = aUnstableParticle -> daughterList().size();
    if (numberOfDaughters > 1) return aUnstableParticle;
    else return findDecayNode(aEvent, & (*aEvent)[aUnstableParticle -> daughterList()[0]]);

    return NULL;
  }

}