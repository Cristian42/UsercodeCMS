#ifndef MyAnalysis_DisplacedJetTrigger_jet_h
#define MyAnalysis_DisplacedJetTrigger_jet_h

#include <vector>
#include "FWCore/Utilities/interface/typedefs.h"
#include "MyAnalysis/DisplacedJetTrigger/interface/track.h"

struct jet {

   double energy,pt,eta,phi;
   std::vector<track> tracks;

};

#endif
