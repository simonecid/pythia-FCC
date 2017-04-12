#!/usr/bin/env python

from ROOT import TFile
from ROOT import TTree
from ROOT import TH1I
from ROOT import TCanvas
from ROOT import TLegend
from math import sqrt
from math import hypot
from sys import argv

import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fileName = argv[1]
higgsFile = TFile(argv[1] + ".root")
higgsDecaysTree = higgsFile.Get("higgsDecays")

numberOfEntries = higgsDecaysTree.GetEntries()

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

higgsPtCanvas = plt.figure()
higgsPtPlot = higgsPtCanvas.add_subplot(1, 1, 1)
ewBosonPtCanvas = plt.figure()
ewBosonPtPlot = ewBosonPtCanvas.add_subplot(1, 1, 1)
ewBosonLeadingPtCanvas = plt.figure()
ewBosonLeadingPtPlot = ewBosonLeadingPtCanvas.add_subplot(1, 1, 1)
ewBosonSubLeadingPtCanvas = plt.figure()
ewBosonSubLeadingPtPlot = ewBosonSubLeadingPtCanvas.add_subplot(1, 1, 1)
ewBoson1PtCanvas = plt.figure()
ewBoson1PtPlot = ewBoson1PtCanvas.add_subplot(1, 1, 1)
ewBoson2PtCanvas = plt.figure()
ewBoson2PtPlot = ewBoson2PtCanvas.add_subplot(1, 1, 1)
chargedLeptonPtCanvas = plt.figure()
chargedLeptonPtPlot = chargedLeptonPtCanvas.add_subplot(1, 1, 1)
neutralLeptonPtCanvas = plt.figure()
neutralLeptonPtPlot = neutralLeptonPtCanvas.add_subplot(1, 1, 1)
lepton1PtCanvas = plt.figure()
lepton1PtPlot = lepton1PtCanvas.add_subplot(1, 1, 1)
lepton2PtCanvas = plt.figure()
lepton2PtPlot = lepton2PtCanvas.add_subplot(1, 1, 1)
lepton3PtCanvas = plt.figure()
lepton3PtPlot = lepton3PtCanvas.add_subplot(1, 1, 1)
lepton4PtCanvas = plt.figure()
lepton4PtPlot = lepton4PtCanvas.add_subplot(1, 1, 1)
higgsEtaCanvas = plt.figure()
higgsEtaPlot = higgsEtaCanvas.add_subplot(1, 1, 1)
ewBosonEtaCanvas = plt.figure()
ewBosonEtaPlot = ewBosonEtaCanvas.add_subplot(1, 1, 1)
chargedLeptonEtaCanvas = plt.figure()
chargedLeptonEtaPlot = chargedLeptonEtaCanvas.add_subplot(1, 1, 1)
higgsPhiCanvas = plt.figure()
higgsPhiPlot = higgsPhiCanvas.add_subplot(1, 1, 1)
ewBosonPhiCanvas = plt.figure()
ewBosonPhiPlot = ewBosonPhiCanvas.add_subplot(1, 1, 1)
chargedLeptonPhiCanvas = plt.figure()
chargedLeptonPhiPlot = chargedLeptonPhiCanvas.add_subplot(1, 1, 1)

''' Histogram with the pt distribution of the Higgs bosons'''
higgsPtN, higgsPtBins, higgsPtPatches = higgsPtPlot.hist(higgsPtData, bins=100, histtype="step")
''' Histogram with the Cumulative pt distribution of both EW bosons'''
ewBosonPtN, ewBosonPtBins, ewBosonPtPatches = ewBosonPtPlot.hist(ewBosonPtData, bins=100, histtype="step")
''' Histogram with the Leading pt distribution of EW bosons'''
ewBosonLeadingPtN, ewBosonLeadingPtBins, ewBosonLeadingPtPatches = ewBosonLeadingPtPlot.hist(ewBosonLeadingPtData, bins=100, histtype="step") 
''' Histogram with the Sub-leading pt distribution of EW bosons'''
ewBosonSubLeadingPtN, ewBosonSubLeadingPtBins, ewBosonSubLeadingPtPatches = ewBosonSubLeadingPtPlot.hist(ewBosonSubLeadingPtData, bins=100, histtype="step")
''' Histogram with the Plot of the distribution of the pt of one the two EW boson, to check that everything is working fine'''
ewBoson1PtN, ewBoson1PtBins, ewBoson1PtPatches = ewBoson1PtPlot.hist(ewBoson1PtData, bins=100, histtype="step") 
''' Histogram with the Plot of the distribution of the pt of one the two EW boson, to check that everything is working fine'''
ewBoson2PtN, ewBoson2PtBins, ewBoson2PtPatches = ewBoson2PtPlot.hist(ewBoson2PtData, bins=100, histtype="step") 
''' Histogram with the Cumulative plot of the distribution of the pt of every charged lepton'''
chargedLeptonPtN, chargedLeptonPtBins, chargedLeptonPtPatches = chargedLeptonPtPlot.hist(chargedLeptonPtData, bins=100, histtype="step") 
''' Histogram with the Cumulative plot of the distribution of the pt of every neutral lepton'''
neutralLeptonPtN, neutralLeptonPtBins, neutralLeptonPtPatches = neutralLeptonPtPlot.hist(neutralLeptonPtData, bins=100, histtype="step") 
''' Histogram with the the distribution of the pt of a lepton'''
lepton1PtN, lepton1PtBins, lepton1PtPatches = lepton1PtPlot.hist(lepton1PtData, bins=100, histtype="step") 
''' Histogram with the the distribution of the pt of a lepton'''
lepton2PtN, lepton2PtBins, lepton2PtPatches = lepton2PtPlot.hist(lepton2PtData, bins=100, histtype="step") 
''' Histogram with the distribution of the pt of a lepton'''
lepton3PtN, lepton3PtBins, lepton3PtPatches = lepton3PtPlot.hist(lepton3PtData, bins=100, histtype="step") 
''' Histogram with the distribution of the pt of a lepton'''
lepton4PtN, lepton4PtBins, lepton4PtPatches = lepton4PtPlot.hist(lepton4PtData, bins=100, histtype="step") 
''' Histogram with the Eta distribution of the Higgs bosons'''
higgsEtaN, higgsEtaBins, higgsEtaPatches = higgsEtaPlot.hist(higgsEtaData, bins=100, histtype="step") #"higgs eta distribution", 100, -10, +10)
''' Histogram with the Cumulative eta distribution of both EW bosons'''
ewBosonEtaN, ewBosonEtaBins, ewBosonEtaPatches = ewBosonEtaPlot.hist(ewBosonEtaData, bins=100, histtype="step") #"EW Boson eta distribution", 100, -10, +10)
''' Histogram with the Cumulative eta distribution of both charged leptons'''
chargedLeptonEtaN, chargedLeptonEtaBins, chargedLeptonEtaPatches = chargedLeptonEtaPlot.hist(chargedLeptonEtaData, bins=100, histtype="step") #"Charged leptons eta distribution", 100, -10, +10)
''' Histogram with the Phi distribution of the Higgs bosons'''
higgsPhiN, higgsPhiBins, higgsPhiPatches = higgsPhiPlot.hist(higgsPhiData, bins=100, histtype="step") #"Higgs phi distribution", 110, -3.30, +3.30)
''' Histogram with the Cumulative phi distribution of both EW bosons'''
ewBosonPhiN, ewBosonPhiBins, ewBosonPhiPatches = ewBosonPhiPlot.hist(ewBosonPhiData, bins=100, histtype="step") #"EW Boson phi distribution", 110, -3.30, +3.30)
''' Histogram with the Cumulative phi distribution of both charged leptons'''
chargedLeptonPhiN, chargedLeptonPhiBins, chargedLeptonPhiPatches = chargedLeptonPhiPlot.hist(chargedLeptonPhiData, bins=100, histtype="step") #"Charged leptons phi distribution", 110, -3.30, +3.30)

higgsPtPlot.set_xlabel("pt [GeV]")
higgsPtPlot.set_ylabel("Counts")
higgsPtPlot.set_title("Higgs boson pt distribution")
higgsPtPlot.grid(True)

ewBosonPtPlot.set_xlabel("pt [GeV]")
ewBosonPtPlot.set_ylabel("Counts")
ewBosonPtPlot.set_title("EW bosons pt distribution")
ewBosonPtPlot.grid(True)

ewBosonLeadingPtPlot.set_xlabel("pt [GeV]")
ewBosonLeadingPtPlot.set_ylabel("Counts")
ewBosonLeadingPtPlot.set_title("EW boson leading pt distribution")
ewBosonLeadingPtPlot.grid(True)

ewBosonSubLeadingPtPlot.set_xlabel("pt [GeV]")
ewBosonSubLeadingPtPlot.set_ylabel("Counts")
ewBosonSubLeadingPtPlot.set_title("EW Boson sub-leading pt distribution")
ewBosonSubLeadingPtPlot.grid(True)

ewBoson1PtPlot.set_xlabel("pt [GeV]")
ewBoson1PtPlot.set_ylabel("Counts")
ewBoson1PtPlot.set_title("EW Boson pt distribution")
ewBoson1PtPlot.grid(True)

ewBoson2PtPlot.set_xlabel("pt [GeV]")
ewBoson2PtPlot.set_ylabel("Counts")
ewBoson2PtPlot.set_title("EW Boson pt distribution")
ewBoson2PtPlot.grid(True)

chargedLeptonPtPlot.set_xlabel("pt [GeV]")
chargedLeptonPtPlot.set_ylabel("Counts")
chargedLeptonPtPlot.set_title("Charged leptons pt distribution")
chargedLeptonPtPlot.grid(True)

neutralLeptonPtPlot.set_xlabel("pt [GeV]")
neutralLeptonPtPlot.set_ylabel("Counts")
neutralLeptonPtPlot.set_title("Neutral leptons pt distribution")
neutralLeptonPtPlot.grid(True)

lepton1PtPlot.set_xlabel("pt [GeV]")
lepton1PtPlot.set_ylabel("Counts")
lepton1PtPlot.set_title("Lepton 1 pt distribution")
lepton1PtPlot.grid(True)

lepton2PtPlot.set_xlabel("pt [GeV]")
lepton2PtPlot.set_ylabel("Counts")
lepton2PtPlot.set_title("Lepton 2 pt distribution")
lepton2PtPlot.grid(True)

lepton3PtPlot.set_xlabel("pt [GeV]")
lepton3PtPlot.set_ylabel("Counts")
lepton3PtPlot.set_title("Lepton 3 pt distribution")
lepton3PtPlot.grid(True)

lepton4PtPlot.set_xlabel("pt [GeV]")
lepton4PtPlot.set_ylabel("Counts")
lepton4PtPlot.set_title("Lepton 4 pt distribution")
lepton4PtPlot.grid(True)

higgsEtaPlot.set_xlabel("$\eta$")
higgsEtaPlot.set_ylabel("Counts")
higgsEtaPlot.set_title("Higgs boson $\eta$ distribution")
higgsEtaPlot.grid(True)

ewBosonEtaPlot.set_xlabel("$\eta$")
ewBosonEtaPlot.set_ylabel("Counts")
ewBosonEtaPlot.set_title("EW bosons $\eta$ distribution")
ewBosonEtaPlot.grid(True)

chargedLeptonEtaPlot.set_xlabel("$\eta$")
chargedLeptonEtaPlot.set_ylabel("Counts")
chargedLeptonEtaPlot.set_title("Charged leptons $\eta$ distribution")
chargedLeptonEtaPlot.grid(True)

higgsPhiPlot.set_xlabel("$\phi$")
higgsPhiPlot.set_ylabel("Counts")
higgsPhiPlot.set_title("Higgs boson $\phi$ distribution")
higgsPhiPlot.grid(True)

ewBosonPhiPlot.set_xlabel("$\phi$")
ewBosonPhiPlot.set_ylabel("Counts")
ewBosonPhiPlot.set_title("EW bosons $\phi$ distribution")
ewBosonPhiPlot.grid(True)

chargedLeptonPhiPlot.set_xlabel("$\phi$")
chargedLeptonPhiPlot.set_ylabel("Counts")
chargedLeptonPhiPlot.set_title("Charged leptons $\phi$ distribution")
chargedLeptonPhiPlot.grid(True)

plt.show()


'''

canvas.SetLogy()
higgsPtHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_higgsPtHisto.png", "png")
ewBosonPtHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_EWBosonPtHisto.png", "png")
ewBosonLeadingPtHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_EWLeadingPtHisto.png", "png")
ewBosonSubLeadingPtHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_EWSubLeadingPtHisto.png", "png")
chargedLeptonPtHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_ChargedLeptonsPtHisto.png", "png")
neutralLeptonPtHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_NeutralLeptonsPtHisto.png", "png")


# EW Boson 1 + EW Boson 2 + total distribution
ewBoson1PtHisto.SetLineColor(2)
ewBoson2PtHisto.SetLineColor(3)
ewBosonPtHisto.Draw()
ewBoson1PtHisto.Draw("SAME")
ewBoson2PtHisto.Draw("SAME")
leg1 = TLegend(0.7,0.7,0.48,0.9)
leg1.SetHeader("Momentum distribution")
leg1.AddEntry(ewBosonPtHisto,"EW boson 1 + EW Boson 2","l")
leg1.AddEntry(ewBoson1PtHisto,"EW Boson 1","l")
leg1.AddEntry(ewBoson2PtHisto,"EW Boson 2","l")
leg1.Draw()
canvas.Update()
canvas.Print(argv[1] + "_EWBosonPtHistogramComparison_1.png", "png")

# Leading + sub-leading + total distribution
ewBosonLeadingPtHisto.SetLineColor(2)
ewBosonSubLeadingPtHisto.SetLineColor(3)
ewBosonPtHisto.Draw()
ewBosonLeadingPtHisto.Draw("SAME")
ewBosonSubLeadingPtHisto.Draw("SAME")
leg2 = TLegend(0.7,0.7,0.48,0.9)
leg2.SetHeader("Momentum distribution")
leg2.AddEntry(ewBosonPtHisto,"Leading+sub-leading","l")
leg2.AddEntry(ewBosonLeadingPtHisto,"Leading pt","l")
leg2.AddEntry(ewBosonSubLeadingPtHisto,"Sub-leading pt","l")
leg2.Draw()
canvas.Update()
canvas.Print(argv[1] + "_EWBosonPtHistogramComparison_2.png", "png")

# Pt of the four leptons
lepton2PtHisto.SetLineColor(2)
lepton3PtHisto.SetLineColor(3)
lepton4PtHisto.SetLineColor(6)
lepton1PtHisto.Draw()
lepton2PtHisto.Draw("SAME")
lepton3PtHisto.Draw("SAME")
lepton4PtHisto.Draw("SAME")
leg3 = TLegend(0.7,0.7,0.48,0.9)
leg3.SetHeader("Momentum distribution")
leg3.AddEntry(lepton1PtHisto,"Lepton 1","l")
leg3.AddEntry(lepton2PtHisto,"Lepton 2","l")
leg3.AddEntry(lepton3PtHisto,"Lepton 3","l")
leg3.AddEntry(lepton4PtHisto,"Lepton 4","l")
leg3.Draw()
canvas.Update()
canvas.Print(argv[1] + "_LeptonPtHistogramComparison.png", "png")

# Eta distributions
higgsEtaHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_higgsEtaHisto.png", "png")
ewBosonEtaHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_decayEtaHisto.png", "png")
chargedLeptonEtaHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_ChargedLeptonEtaHisto.png", "png")

# Phi distributions
higgsPhiHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_higgsPhiHisto.png", "png")
ewBosonPhiHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_decayPhiHisto.png", "png")
chargedLeptonPhiHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_ChargedLeptonPhiHisto.png", "png")

'''