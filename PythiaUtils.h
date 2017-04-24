#ifndef PYTHIAUTILS_H
#define PYTHIAUTILS_H

#include "Pythia8/Pythia.h"

namespace PythiaUtils{

  /**
    Browse through the particle list of a Pythia event to find the Pythia8::Particle object which decays 
    and does not the propagated.
    Since I like when stuff blows up in my hands I use recursion, w8ing 4 a stack overflow <3.
  */
  const Pythia8::Particle* findDecayNode(const Pythia8::Event* aEvent, const Pythia8::Particle* aUnstableParticle)
  {
    const unsigned int lNumberOfDaughters = aUnstableParticle -> daughterList().size();
    const int lUnstableParticlePGDID = aUnstableParticle -> id();

    if (lNumberOfDaughters > 1) {
      //Might be a bremsstrahlung event, or any kind of emission. I check if my original particle is still there

      const Pythia8::Particle * lDecayProducts[2];
      lDecayProducts[0] = & (*aEvent)[aUnstableParticle -> daughterList()[0]];
      lDecayProducts[1] = & (*aEvent)[aUnstableParticle -> daughterList()[1]];
      if (lDecayProducts[0] -> id() == lUnstableParticlePGDID) {
        // We have an emission event, I still have to look for the decay node
        return findDecayNode(aEvent, lDecayProducts[0]);
      }
      if (lDecayProducts[1] -> id() == lUnstableParticlePGDID) {
        // We have an emission event, I still have to look for the decay node
        return findDecayNode(aEvent, lDecayProducts[1]);
      }
      return aUnstableParticle;
    }
    else return findDecayNode(aEvent, & (*aEvent)[aUnstableParticle -> daughterList()[0]]);
    
    return NULL;
  }

}

#endif //  PYTHIAUTILS_H