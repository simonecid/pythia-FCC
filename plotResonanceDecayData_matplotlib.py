#!/usr/bin/env python

from ROOT import TFile
from ROOT import TTree
from math import sqrt
from math import hypot
from sys import argv

import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fileName = argv[1]
resonanceFile = TFile(fileName + ".root")
resonanceDecaysTree = resonanceFile.Get("resonanceDecays")

numberOfEntries = resonanceDecaysTree.GetEntries()

# ---- Preparing the data containers ---- 

'''Contains the pt distribution of the resonances'''
resonancePtData = [] # = TH1I("resonancePtHisto", "Resonance pt distribution", 100, 0, 500)
'''Contains the pt distribution of both decay products'''
decayPtData = [] # = TH1I("decayPtHisto", "Decay products pt distribution", 100, 0, 500)
'''Contains the leading pt distribution of the decay products'''
decayLeadingPtData = [] # = TH1I("decayLeadingPtHisto", "Decay product leading pt distribution", 100, 0, 500)
'''Contains the sub-leading pt distribution of the decay products'''
decaySubLeadingPtData = [] # = TH1I("decaySubLeadingPtHisto", "Decay product sub-leading pt distribution", 100, 0, 500)
'''Contains the pt distribution of a decay product'''
decay1PtData = []
'''Contains the pt distribution of a decay product'''
decay2PtData = []

'''Contains the eta distribution of the resonances'''
resonanceEtaData = [] # = TH1I("resonanceEtaHisto", "Resonance eta distribution", 100, -10, +10)
'''Contains the eta distribution of both decay products'''
decayEtaData = [] # = TH1I("decayEtaHisto", "Decay products eta distribution", 100, -10, +10)

'''Contains the phi distribution of the resonances'''
resonancePhiData = [] # = TH1I("resonancePhiHisto", "Resonance phi distribution", 110, -3.30, +3.30)
'''Contains the phi distribution of both decay products'''
decayPhiData = [] # = TH1I("decayPhiHisto", "Decay product phi distribution", 110, -3.30, +3.30)

# ---- Retrieving event data ----

for eventIndex in xrange(0, numberOfEntries):
  resonanceDecaysTree.GetEntry(eventIndex)
  
  # Retrieving Pt
  resonancePt = hypot(resonanceDecaysTree.resonancePx, resonanceDecaysTree.resonancePy)
  decay1Pt = hypot(resonanceDecaysTree.decay1Px, resonanceDecaysTree.decay1Py)
  decay2Pt = hypot(resonanceDecaysTree.decay2Px, resonanceDecaysTree.decay2Py)

  leadingPt = max(decay1Pt, decay2Pt)
  subLeadingPt = min(decay1Pt, decay2Pt)

  # Retrieving eta
  resonanceEta = resonanceDecaysTree.resonanceEta
  decay1Eta = resonanceDecaysTree.decay1Eta
  decay2Eta = resonanceDecaysTree.decay2Eta

  # Retrieving phi
  resonancePhi = resonanceDecaysTree.resonancePhi
  decay1Phi = resonanceDecaysTree.decay1Phi
  decay2Phi = resonanceDecaysTree.decay2Phi

  # Filling the histogram

  resonancePtData.append(resonancePt)
  decayPtData.append(decay1Pt)
  decayPtData.append(decay2Pt)
  decay1PtData.append(decay1Pt)
  decay2PtData.append(decay2Pt)
  decayLeadingPtData.append(leadingPt)
  decaySubLeadingPtData.append(subLeadingPt)

  resonanceEtaData.append(resonanceEta)
  decayEtaData.append(decay1Eta)
  decayEtaData.append(decay2Eta)

  resonancePhiData.append(resonancePhi)
  decayPhiData.append(decay1Phi)
  decayPhiData.append(decay2Phi)

# ---- Creating canvases and plot objects

resonancePtCanvas = plt.figure()
resonancePtPlot = resonancePtCanvas.add_subplot(1, 1, 1)
decayPtCanvas = plt.figure()
decayPtPlot = decayPtCanvas.add_subplot(1, 1, 1)
decaysPtCanvas = plt.figure()
decaysPtPlot = decaysPtCanvas.add_subplot(1, 1, 1)
decayLeadingPtCanvas = plt.figure()
decayLeadingPtPlot = decayLeadingPtCanvas.add_subplot(1, 1, 1)
decaySubLeadingPtCanvas = plt.figure()
decaySubLeadingPtPlot = decaySubLeadingPtCanvas.add_subplot(1, 1, 1)

resonanceEtaCanvas = plt.figure()
resonanceEtaPlot = resonanceEtaCanvas.add_subplot(1, 1, 1)
decayEtaCanvas = plt.figure()
decayEtaPlot = decayEtaCanvas.add_subplot(1, 1, 1)

resonancePhiCanvas = plt.figure()
resonancePhiPlot = resonancePhiCanvas.add_subplot(1, 1, 1)
decayPhiCanvas = plt.figure()
decayPhiPlot = decayPhiCanvas.add_subplot(1, 1, 1)

# ---- Building up plots ----

resonancePtPlot.hist(resonancePtData, bins=100, histtype="step")
decayPtPlot.hist(decayPtData, bins=100, histtype="step")
decaysPtPlot.hist(decay1PtData, bins=100, histtype="step", label="Decay 1")
decaysPtPlot.hist(decay2PtData, bins=100, histtype="step", label="Decay 2")
decayLeadingPtPlot.hist(decayLeadingPtData, bins=100, histtype="step")
decaySubLeadingPtPlot.hist(decaySubLeadingPtData, bins=100, histtype="step")
resonanceEtaPlot.hist(resonanceEtaData, bins=100, histtype="step")
decayEtaPlot.hist(decayEtaData, bins=100, histtype="step")
resonancePhiPlot.hist(resonancePhiData, bins=100, histtype="step")
decayPhiPlot.hist(decayPhiData, bins=100, histtype="step")

# ---- Setting up and drawing the plots ----

# pt stuff

resonancePtPlot.set_xlabel("pt [GeV]")
resonancePtPlot.set_ylabel("Counts")
resonancePtPlot.set_title("Resonance pt distribution")
resonancePtPlot.grid(True)
resonancePtPlot.set_yscale('log')
print "Saving to " + fileName + "_resonancePtPlot.svg"
resonancePtCanvas.savefig(fileName + "_resonancePtPlot.svg")
print "Saved!"


decayPtPlot.set_xlabel("pt [GeV]")
decayPtPlot.set_ylabel("Counts")
decayPtPlot.set_title("Resonance pt distribution")
decayPtPlot.grid(True)
decayPtPlot.set_yscale('log')
print "Saving to " + fileName + "_decayPtPlot.svg"
decayPtCanvas.savefig(fileName + "_decayPtPlot.svg")
print "Saved!"

decaysPtPlot.set_xlabel("pt [GeV]")
decaysPtPlot.set_ylabel("Counts")
decaysPtPlot.set_title("Resonance pt distribution")
decaysPtPlot.grid(True)
decaysPtPlot.set_yscale('log')
decaysPtPlot.legend(loc="upper right")
print "Saving to " + fileName + "_decaysPtPlot.svg"
decaysPtCanvas.savefig(fileName + "_decaysPtPlot.svg")
print "Saved!"

decayLeadingPtPlot.set_xlabel("pt [GeV]")
decayLeadingPtPlot.set_ylabel("Counts")
decayLeadingPtPlot.set_title("Resonance pt distribution")
decayLeadingPtPlot.grid(True)
decayLeadingPtPlot.set_yscale('log')
print "Saving to " + fileName + "_decayLeadingPtPlot.svg"
decayLeadingPtCanvas.savefig(fileName + "_decayLeadingPtPlot.svg")
print "Saved!"

decaySubLeadingPtPlot.set_xlabel("pt [GeV]")
decaySubLeadingPtPlot.set_ylabel("Counts")
decaySubLeadingPtPlot.set_title("Resonance pt distribution")
decaySubLeadingPtPlot.grid(True)
decaySubLeadingPtPlot.set_yscale('log')
print "Saving to " + fileName + "_decaySubLeadingPtPlot.svg"
decaySubLeadingPtCanvas.savefig(fileName + "_decaySubLeadingPtPlot.svg")
print "Saved!"

# Eta

resonanceEtaPlot.set_xlabel("pt [GeV]")
resonanceEtaPlot.set_ylabel("Counts")
resonanceEtaPlot.set_title("Resonance pt distribution")
resonanceEtaPlot.grid(True)
resonanceEtaPlot.set_yscale('log')
print "Saving to " + fileName + "_resonanceEtaPlot.svg"
resonanceEtaCanvas.savefig(fileName + "_resonanceEtaPlot.svg")
print "Saved!"

decayEtaPlot.set_xlabel("pt [GeV]")
decayEtaPlot.set_ylabel("Counts")
decayEtaPlot.set_title("Resonance pt distribution")
decayEtaPlot.grid(True)
decayEtaPlot.set_yscale('log')
print "Saving to " + fileName + "_decayEtaPlot.svg"
decayEtaCanvas.savefig(fileName + "_decayEtaPlot.svg")
print "Saved!"

# Phi

resonancePhiPlot.set_xlabel("pt [GeV]")
resonancePhiPlot.set_ylabel("Counts")
resonancePhiPlot.set_title("Resonance pt distribution")
resonancePhiPlot.grid(True)
resonancePhiPlot.set_yscale('log')
print "Saving to " + fileName + "_resonancePhiPlot.svg"
resonancePhiCanvas.savefig(fileName + "_resonancePhiPlot.svg")
print "Saved!"

decayPhiPlot.set_xlabel("pt [GeV]")
decayPhiPlot.set_ylabel("Counts")
decayPhiPlot.set_title("Resonance pt distribution")
decayPhiPlot.grid(True)
decayPhiPlot.set_yscale('log')
print "Saving to " + fileName + "_decayPhiPlot.svg"
decayPhiCanvas.savefig(fileName + "_decayPhiPlot.svg")
print "Saved!"

#plt.show()