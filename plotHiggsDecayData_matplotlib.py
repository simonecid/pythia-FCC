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
higgsFile = TFile(fileName + ".root")
higgsDecaysTree = higgsFile.Get("higgsDecays")

numberOfEntries = higgsDecaysTree.GetEntries()

# ---- Preparing data container structures ----

''' Array with the pt distribution of the Higgs bosons'''
higgsPtData = []
''' Array with the Cumulative pt distribution of both EW bosons'''
ewBosonPtData = []
''' Array with the Leading pt distribution of EW bosons'''
ewBosonLeadingPtData = []
''' Array with the Sub-leading pt distribution of EW bosons'''
ewBosonSubLeadingPtData = []
''' Array with the distribution of the pt of one the two EW boson, to check that everything is working fine'''
ewBoson1PtData = []
''' Array with the distribution of the pt of one the two EW boson, to check that everything is working fine'''
ewBoson2PtData = []
''' Array with the distribution of the pt of every charged lepton'''
chargedLeptonPtData = []
''' Array with the distribution of the pt of every neutral lepton'''
neutralLeptonPtData = []
''' Array with the distribution of the pt of a lepton'''
lepton1PtData = []
''' Array with the distribution of the pt of a lepton'''
lepton2PtData = []
''' Array with the distribution of the pt of a lepton'''
lepton3PtData = []
''' Array with the distribution of the pt of a lepton'''
lepton4PtData = []

''' Array with the Eta distribution of the Higgs bosons'''
higgsEtaData = []
''' Array with the Cumulative eta distribution of both EW bosons'''
ewBosonEtaData = []
''' Array with the Cumulative eta distribution of both charged leptons'''
chargedLeptonEtaData = []

''' Array with the Phi distribution of the Higgs bosons'''
higgsPhiData = []
''' Array with the Cumulative phi distribution of both EW bosons'''
ewBosonPhiData = []
''' Array with the Cumulative phi distribution of both charged leptons'''
chargedLeptonPhiData = []

# ---- Retrieving event data ----

for eventIndex in xrange(0, numberOfEntries):
  higgsDecaysTree.GetEntry(eventIndex)
  
  # Retrieving Pt
  higgsPt = hypot(higgsDecaysTree.higgsPx, higgsDecaysTree.higgsPy)
  ewBoson1Pt = hypot(higgsDecaysTree.ewBoson1Px, higgsDecaysTree.ewBoson1Py)
  ewBoson2Pt = hypot(higgsDecaysTree.ewBoson2Px, higgsDecaysTree.ewBoson2Py)

  lepton1Pt = hypot(higgsDecaysTree.lepton1Px, higgsDecaysTree.lepton1Py)
  lepton2Pt = hypot(higgsDecaysTree.lepton2Px, higgsDecaysTree.lepton2Py)
  lepton3Pt = hypot(higgsDecaysTree.lepton3Px, higgsDecaysTree.lepton3Py)
  lepton4Pt = hypot(higgsDecaysTree.lepton4Px, higgsDecaysTree.lepton4Py)

  leadingEWBosonPt = max(ewBoson1Pt, ewBoson2Pt)
  subLeadingEWBosonPt = min(ewBoson1Pt, ewBoson2Pt)

  # Retrieving eta
  higgsEta = higgsDecaysTree.higgsEta
  ewBoson1Eta = higgsDecaysTree.ewBoson1Eta
  ewBoson2Eta = higgsDecaysTree.ewBoson2Eta
  lepton1Eta = higgsDecaysTree.lepton1Eta
  lepton2Eta = higgsDecaysTree.lepton2Eta
  lepton3Eta = higgsDecaysTree.lepton3Eta
  lepton4Eta = higgsDecaysTree.lepton4Eta

  # Retrieving phi
  higgsPhi = higgsDecaysTree.higgsPhi
  ewBoson1Phi = higgsDecaysTree.ewBoson1Phi
  ewBoson2Phi = higgsDecaysTree.ewBoson2Phi
  lepton1Phi = higgsDecaysTree.lepton1Phi
  lepton2Phi = higgsDecaysTree.lepton2Phi
  lepton3Phi = higgsDecaysTree.lepton3Phi
  lepton4Phi = higgsDecaysTree.lepton4Phi

  # Retrieving lepton PDGID

  lepton1PDGID = higgsDecaysTree.lepton1PDGID
  lepton2PDGID = higgsDecaysTree.lepton2PDGID
  lepton3PDGID = higgsDecaysTree.lepton3PDGID
  lepton4PDGID = higgsDecaysTree.lepton4PDGID

  # Checking if charged lepton
  chargedLeptonsPDGID = [11, 13, 15]
  isLepton1Charged = lepton1PDGID in chargedLeptonsPDGID
  isLepton2Charged = lepton2PDGID in chargedLeptonsPDGID
  isLepton3Charged = lepton3PDGID in chargedLeptonsPDGID
  isLepton4Charged = lepton4PDGID in chargedLeptonsPDGID

  # Filling the histogram

  higgsPtData.append(higgsPt)
  ewBosonPtData.append(ewBoson1Pt)
  ewBosonPtData.append(ewBoson2Pt)
  ewBosonLeadingPtData.append(leadingEWBosonPt)
  ewBosonSubLeadingPtData.append(subLeadingEWBosonPt)
  ewBoson1PtData.append(ewBoson1Pt)
  ewBoson2PtData.append(ewBoson2Pt)
  lepton1PtData.append(lepton1Pt)
  lepton2PtData.append(lepton2Pt)
  lepton3PtData.append(lepton3Pt)
  lepton4PtData.append(lepton4Pt)
  if isLepton1Charged : chargedLeptonPtData.append(lepton1Pt)
  if isLepton2Charged : chargedLeptonPtData.append(lepton2Pt)
  if isLepton3Charged : chargedLeptonPtData.append(lepton3Pt)
  if isLepton4Charged : chargedLeptonPtData.append(lepton4Pt)
  if not isLepton1Charged : neutralLeptonPtData.append(lepton1Pt)
  if not isLepton2Charged : neutralLeptonPtData.append(lepton2Pt)
  if not isLepton3Charged : neutralLeptonPtData.append(lepton3Pt)
  if not isLepton4Charged : neutralLeptonPtData.append(lepton4Pt)
  
  higgsEtaData.append(higgsEta)
  ewBosonEtaData.append(ewBoson1Eta)
  ewBosonEtaData.append(ewBoson2Eta)
  if isLepton1Charged : chargedLeptonEtaData.append(lepton1Eta)
  if isLepton2Charged : chargedLeptonEtaData.append(lepton2Eta)
  if isLepton3Charged : chargedLeptonEtaData.append(lepton3Eta)
  if isLepton4Charged : chargedLeptonEtaData.append(lepton4Eta)

  higgsPhiData.append(higgsPhi)
  ewBosonPhiData.append(ewBoson1Phi)
  ewBosonPhiData.append(ewBoson2Phi)
  if isLepton1Charged : chargedLeptonPhiData.append(lepton1Phi)
  if isLepton2Charged : chargedLeptonPhiData.append(lepton2Phi)
  if isLepton3Charged : chargedLeptonPhiData.append(lepton3Phi)
  if isLepton4Charged : chargedLeptonPhiData.append(lepton4Phi)


# ---- Creating canvases (window) and plot objects ----

higgsPtCanvas = plt.figure()
''' Histogram with the pt distribution of the Higgs bosons'''
higgsPtPlot = higgsPtCanvas.add_subplot(1, 1, 1)
ewBosonPtCanvas = plt.figure()
''' Histogram with the Cumulative pt distribution of both EW bosons'''
ewBosonPtPlot = ewBosonPtCanvas.add_subplot(1, 1, 1)
ewBosonLeadingPtCanvas = plt.figure()
''' Histogram with the Leading pt distribution of EW bosons'''
ewBosonLeadingPtPlot = ewBosonLeadingPtCanvas.add_subplot(1, 1, 1)
ewBosonSubLeadingPtCanvas = plt.figure()
''' Histogram with the Sub-leading pt distribution of EW bosons'''
ewBosonSubLeadingPtPlot = ewBosonSubLeadingPtCanvas.add_subplot(1, 1, 1)
ewBosonsPtCanvas = plt.figure()
ewBosonsPtPlot = ewBosonsPtCanvas.add_subplot(1, 1, 1)
chargedLeptonPtCanvas = plt.figure()
''' Histogram with the Cumulative plot of the distribution of the pt of every charged lepton'''
chargedLeptonPtPlot = chargedLeptonPtCanvas.add_subplot(1, 1, 1)
neutralLeptonPtCanvas = plt.figure()
''' Histogram with the Cumulative plot of the distribution of the pt of every neutral lepton'''
neutralLeptonPtPlot = neutralLeptonPtCanvas.add_subplot(1, 1, 1)
leptonsPtCanvas = plt.figure()
''' Histogram with the the distributions of the pt of the four leptons'''
leptonsPtPlot = leptonsPtCanvas.add_subplot(1, 1, 1)
higgsEtaCanvas = plt.figure()
''' Histogram with the Eta distribution of the Higgs bosons'''
higgsEtaPlot = higgsEtaCanvas.add_subplot(1, 1, 1)
ewBosonEtaCanvas = plt.figure()
''' Histogram with the Cumulative eta distribution of both EW bosons'''
ewBosonEtaPlot = ewBosonEtaCanvas.add_subplot(1, 1, 1)
chargedLeptonEtaCanvas = plt.figure()
''' Histogram with the Cumulative eta distribution of both charged leptons'''
chargedLeptonEtaPlot = chargedLeptonEtaCanvas.add_subplot(1, 1, 1)
higgsPhiCanvas = plt.figure()
''' Histogram with the Phi distribution of the Higgs bosons'''
higgsPhiPlot = higgsPhiCanvas.add_subplot(1, 1, 1)
ewBosonPhiCanvas = plt.figure()
''' Histogram with the Cumulative phi distribution of both EW bosons'''
ewBosonPhiPlot = ewBosonPhiCanvas.add_subplot(1, 1, 1)
chargedLeptonPhiCanvas = plt.figure()
''' Histogram with the Cumulative phi distribution of both charged leptons'''
chargedLeptonPhiPlot = chargedLeptonPhiCanvas.add_subplot(1, 1, 1)


# ---- Building up plots ----

higgsPtPlot.hist(higgsPtData, bins=100, histtype="step")
ewBosonPtPlot.hist(ewBosonPtData, bins=100, histtype="step")
ewBosonLeadingPtPlot.hist(ewBosonLeadingPtData, bins=100, histtype="step") 
ewBosonSubLeadingPtPlot.hist(ewBosonSubLeadingPtData, bins=100, histtype="step")

# EW Boson 1 +  EW Boson 2 + Total
ewBosonsPtPlot.hist(ewBoson1PtData, bins=100, histtype="step", label="EW Boson 1")
ewBosonsPtPlot.hist(ewBoson2PtData, bins=100, histtype="step", label="EW Boson 2")
ewBosonsPtPlot.hist(ewBosonPtData, bins=100, histtype="step", label="EW Boson 1 + 2")

chargedLeptonPtN, chargedLeptonPtBins, chargedLeptonPtPatches = chargedLeptonPtPlot.hist(chargedLeptonPtData, bins=100, histtype="step") 
neutralLeptonPtN, neutralLeptonPtBins, neutralLeptonPtPatches = neutralLeptonPtPlot.hist(neutralLeptonPtData, bins=100, histtype="step") 

# Four leptons
leptonsPtPlot.hist(lepton1PtData, bins=100, histtype="step", label="Lepton 1") 
leptonsPtPlot.hist(lepton2PtData, bins=100, histtype="step", label="Lepton 2") 
leptonsPtPlot.hist(lepton3PtData, bins=100, histtype="step", label="Lepton 3") 
leptonsPtPlot.hist(lepton4PtData, bins=100, histtype="step", label="Lepton 4") 

# Eta stuff
higgsEtaPlot.hist(higgsEtaData, bins=100, histtype="step")
ewBosonEtaPlot.hist(ewBosonEtaData, bins=100, histtype="step")
chargedLeptonEtaPlot.hist(chargedLeptonEtaData, bins=100, histtype="step")

# Phi stuff
higgsPhiPlot.hist(higgsPhiData, bins=100, histtype="step")
ewBosonPhiPlot.hist(ewBosonPhiData, bins=100, histtype="step")
chargedLeptonPhiPlot.hist(chargedLeptonPhiData, bins=100, histtype="step")

# ---- Setting up, drawing, and saving plots ----

higgsPtPlot.set_xlabel("pt [GeV]")
higgsPtPlot.set_ylabel("Counts")
higgsPtPlot.set_title("Higgs boson pt distribution")
higgsPtPlot.grid(True)
higgsPtPlot.legend(loc="upper right")
higgsPtCanvas.savefig(fileName + "_higgsPtPlot.svg")

ewBosonPtPlot.set_xlabel("pt [GeV]")
ewBosonPtPlot.set_ylabel("Counts")
ewBosonPtPlot.set_title("EW bosons pt distribution")
ewBosonPtPlot.grid(True)
ewBosonPtPlot.legend(loc="upper right")
ewBosonPtCanvas.savefig(fileName + "_ewBosonPtPlot.svg")

ewBosonLeadingPtPlot.set_xlabel("pt [GeV]")
ewBosonLeadingPtPlot.set_ylabel("Counts")
ewBosonLeadingPtPlot.set_title("EW boson leading pt distribution")
ewBosonLeadingPtPlot.grid(True)
ewBosonLeadingPtPlot.legend(loc="upper right")
ewBosonLeadingPtCanvas.savefig(fileName + "_ewBosonLeadingPtPlot.svg")

ewBosonSubLeadingPtPlot.set_xlabel("pt [GeV]")
ewBosonSubLeadingPtPlot.set_ylabel("Counts")
ewBosonSubLeadingPtPlot.set_title("EW Boson sub-leading pt distribution")
ewBosonSubLeadingPtPlot.grid(True)
ewBosonSubLeadingPtPlot.legend(loc="upper right")
ewBosonSubLeadingPtCanvas.savefig(fileName + "_ewBosonSubLeadingPtPlot.svg")

ewBosonsPtPlot.set_xlabel("pt [GeV]")
ewBosonsPtPlot.set_ylabel("Counts")
ewBosonsPtPlot.set_title("EW Bosons pt distribution")
ewBosonsPtPlot.grid(True)
ewBosonsPtPlot.legend(loc="upper right")
ewBosonsPtCanvas.savefig(fileName + "_ewBosonsPtPlot.svg")

chargedLeptonPtPlot.set_xlabel("pt [GeV]")
chargedLeptonPtPlot.set_ylabel("Counts")
chargedLeptonPtPlot.set_title("Charged leptons pt distribution")
chargedLeptonPtPlot.grid(True)
chargedLeptonPtPlot.legend(loc="upper right")
chargedLeptonPtCanvas.savefig(fileName + "_chargedLeptonPtPlot.svg")

neutralLeptonPtPlot.set_xlabel("pt [GeV]")
neutralLeptonPtPlot.set_ylabel("Counts")
neutralLeptonPtPlot.set_title("Neutral leptons pt distribution")
neutralLeptonPtPlot.grid(True)
neutralLeptonPtPlot.legend(loc="upper right")
neutralLeptonPtCanvas.savefig(fileName + "_neutralLeptonPtPlot.svg")

leptonsPtPlot.set_xlabel("pt [GeV]")
leptonsPtPlot.set_ylabel("Counts")
leptonsPtPlot.set_title("Leptons pt distribution")
leptonsPtPlot.grid(True)
leptonsPtPlot.legend(loc="upper right")
leptonsPtCanvas.savefig(fileName + "_leptonsPtPlot.svg")

higgsEtaPlot.set_xlabel("$\eta$")
higgsEtaPlot.set_ylabel("Counts")
higgsEtaPlot.set_title("Higgs boson $\eta$ distribution")
higgsEtaPlot.grid(True)
higgsEtaPlot.legend(loc="upper right")
higgsEtaCanvas.savefig(fileName + "_higgsEtaPlot.svg")

ewBosonEtaPlot.set_xlabel("$\eta$")
ewBosonEtaPlot.set_ylabel("Counts")
ewBosonEtaPlot.set_title("EW bosons $\eta$ distribution")
ewBosonEtaPlot.grid(True)
ewBosonEtaPlot.legend(loc="upper right")
ewBosonEtaCanvas.savefig(fileName + "_ewBosonEtaPlot.svg")

chargedLeptonEtaPlot.set_xlabel("$\eta$")
chargedLeptonEtaPlot.set_ylabel("Counts")
chargedLeptonEtaPlot.set_title("Charged leptons $\eta$ distribution")
chargedLeptonEtaPlot.grid(True)
chargedLeptonEtaPlot.legend(loc="upper right")
chargedLeptonEtaCanvas.savefig(fileName + "_chargedLeptonEtaPlot.svg")

higgsPhiPlot.set_xlabel("$\phi$")
higgsPhiPlot.set_ylabel("Counts")
higgsPhiPlot.set_title("Higgs boson $\phi$ distribution")
higgsPhiPlot.grid(True)
higgsPhiPlot.legend(loc="upper right")
higgsPhiCanvas.savefig(fileName + "_higgsPhiPlot.svg")

ewBosonPhiPlot.set_xlabel("$\phi$")
ewBosonPhiPlot.set_ylabel("Counts")
ewBosonPhiPlot.set_title("EW bosons $\phi$ distribution")
ewBosonPhiPlot.grid(True)
ewBosonPhiPlot.legend(loc="upper right")
ewBosonPhiCanvas.savefig(fileName + "_ewBosonPhiPlot.svg")

chargedLeptonPhiPlot.set_xlabel("$\phi$")
chargedLeptonPhiPlot.set_ylabel("Counts")
chargedLeptonPhiPlot.set_title("Charged leptons $\phi$ distribution")
chargedLeptonPhiPlot.grid(True)
chargedLeptonPhiPlot.legend(loc="upper right")
chargedLeptonPhiCanvas.savefig(fileName + "_chargedLeptonPhiPlot.svg")