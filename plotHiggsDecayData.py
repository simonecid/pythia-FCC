#!/usr/bin/env python

from ROOT import TFile
from ROOT import TTree
from ROOT import TH1I
from ROOT import TCanvas
from ROOT import TLegend
from math import sqrt
from math import hypot
from sys import argv

fileName = argv[1]
higgsFile = TFile(argv[1] + ".root")
higgsDecaysTree = higgsFile.Get("higgsDecays")

numberOfEntries = higgsDecaysTree.GetEntries()

outputFile = TFile(argv[1] + "_plots" + ".root", "RECREATE")

'''pt distribution of the Higgs bosons'''
higgsPtHisto = TH1I("higgsPtHisto", "Higgs pt distribution", 100, 0, 500)
'''Cumulative pt distribution of both EW bosons'''
ewBosonPtHisto = TH1I("ewBosonPtHisto", "EW Bosons pt distribution", 100, 0, 500)
'''Leading pt distribution of EW bosons'''
ewBosonLeadingPtHisto = TH1I("ewBosonLeadingPtHisto", "EW Boson leading pt distribution", 100, 0, 500)
'''Sub-leading pt distribution of EW bosons'''
ewBosonSubLeadingPtHisto = TH1I("ewBosonSubLeadingPtHisto", "EW Boson sub-leading pt distribution", 100, 0, 500)
'''Plot of the distribution of the pt of one the two EW boson, to check that everything is working fine'''
ewBoson1PtHisto = TH1I("ewBoson1PtHisto", "EW Boson pt distribution", 100, 0, 500)
'''Plot of the distribution of the pt of one the two EW boson, to check that everything is working fine'''
ewBoson2PtHisto = TH1I("ewBoson2PtHisto", "EW Boson pt distribution", 100, 0, 500)
'''Cumulative plot of the distribution of the pt of every charged lepton'''
chargedLeptonPtHisto = TH1I("chargedLeptonPtHisto", "Charged leptons pt distribution", 100, 0, 500)
'''Cumulative plot of the distribution of the pt of every neutral lepton'''
neutralLeptonPtHisto = TH1I("neutralLeptonPtHisto", "Neutral leptons pt distribution", 100, 0, 500)
'''Plot of the distribution of the pt of a lepton'''
lepton1PtHisto = TH1I("lepton1PtHisto", "Lepton 1 pt distribution", 100, 0, 500)
'''Plot of the distribution of the pt of a lepton'''
lepton2PtHisto = TH1I("lepton2PtHisto", "Lepton 2 pt distribution", 100, 0, 500)
'''Plot of the distribution of the pt of a lepton'''
lepton3PtHisto = TH1I("lepton3PtHisto", "Lepton 3 pt distribution", 100, 0, 500)
'''Plot of the distribution of the pt of a lepton'''
lepton4PtHisto = TH1I("lepton4PtHisto", "Lepton 4 pt distribution", 100, 0, 500)
'''Plot of the distribution of the leading pt of the four leptons'''
leadingChargedLeptonPtHisto = TH1I("leadingChargedLeptonPtHisto", "Lepton leading pt distribution", 100, 0, 500)



'''Eta distribution of the Higgs bosons'''
higgsEtaHisto = TH1I("higgsEtaHisto", "higgs eta distribution", 100, -10, +10)
'''Cumulative eta distribution of both EW bosons'''
ewBosonEtaHisto = TH1I("ewBosonEtaHisto", "EW Boson eta distribution", 100, -10, +10)
'''Cumulative eta distribution of both charged leptons'''
chargedLeptonEtaHisto = TH1I("chargedLeptonEtaHisto", "Charged leptons eta distribution", 100, -10, +10)
'''Distribution of eta of the leading pt leptons'''
chargedLeptonLeadingEtaHisto = TH1I("chargedLeptonLeadingEtaHisto", "Leading pt lepton eta distribution", 100, -10, +10)



'''Phi distribution of the Higgs bosons'''
higgsPhiHisto = TH1I("higgsPhiHisto", "Higgs phi distribution", 110, -3.30, +3.30)
'''Cumulative phi distribution of both EW bosons'''
ewBosonPhiHisto = TH1I("ewBosonPhiHisto", "EW Boson phi distribution", 110, -3.30, +3.30)
'''Cumulative phi distribution of both charged leptons'''
chargedLeptonPhiHisto = TH1I("chargedLeptonPhiHisto", "Charged leptons phi distribution", 110, -3.30, +3.30)

chargedLeptonsPDGID = [11, 13, 15, -11, -13, -15]
neutralLeptonsPDGID = [12, 14, 16, -12, -14, -16]

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
  isLepton1Charged = lepton1PDGID in chargedLeptonsPDGID
  isLepton2Charged = lepton2PDGID in chargedLeptonsPDGID
  isLepton3Charged = lepton3PDGID in chargedLeptonsPDGID
  isLepton4Charged = lepton4PDGID in chargedLeptonsPDGID

  leadingChargedLeptonPt = 0
  leadingChargedLeptonPt_Eta = 0

  # Filling the histogram

  higgsPtHisto.Fill(higgsPt)
  ewBosonPtHisto.Fill(ewBoson1Pt)
  ewBosonPtHisto.Fill(ewBoson2Pt)
  ewBosonLeadingPtHisto.Fill(leadingEWBosonPt)
  ewBosonSubLeadingPtHisto.Fill(subLeadingEWBosonPt)
  ewBoson1PtHisto.Fill(ewBoson1Pt)
  ewBoson2PtHisto.Fill(ewBoson2Pt)
  lepton1PtHisto.Fill(lepton1Pt)
  lepton2PtHisto.Fill(lepton2Pt)
  lepton3PtHisto.Fill(lepton3Pt)
  lepton4PtHisto.Fill(lepton4Pt)
  
  if isLepton1Charged : 
    chargedLeptonPtHisto.Fill(lepton1Pt)
    leadingChargedLeptonPt = lepton1Pt
    leadingChargedLeptonPt_Eta = lepton1Eta
  if isLepton2Charged : 
    chargedLeptonPtHisto.Fill(lepton2Pt)
    if lepton2Pt > leadingChargedLeptonPt :
      leadingChargedLeptonPt = lepton2Pt
      leadingChargedLeptonPt_Eta = lepton2Eta
  if isLepton3Charged : 
    chargedLeptonPtHisto.Fill(lepton3Pt)
    if lepton3Pt > leadingChargedLeptonPt :
      leadingChargedLeptonPt = lepton3Pt
      leadingChargedLeptonPt_Eta = lepton3Eta
  if isLepton4Charged : 
    chargedLeptonPtHisto.Fill(lepton4Pt)
    if lepton4Pt > leadingChargedLeptonPt :
      leadingChargedLeptonPt = lepton4Pt
      leadingChargedLeptonPt_Eta = lepton4Eta

  if not isLepton1Charged : neutralLeptonPtHisto.Fill(lepton1Pt)
  if not isLepton2Charged : neutralLeptonPtHisto.Fill(lepton2Pt)
  if not isLepton3Charged : neutralLeptonPtHisto.Fill(lepton3Pt)
  if not isLepton4Charged : neutralLeptonPtHisto.Fill(lepton4Pt)

  if leadingChargedLeptonPt > 0:
    leadingChargedLeptonPtHisto.Fill(leadingChargedLeptonPt)
    chargedLeptonLeadingEtaHisto.Fill(leadingChargedLeptonPt_Eta)
  
  higgsEtaHisto.Fill(higgsEta)
  ewBosonEtaHisto.Fill(ewBoson1Eta)
  ewBosonEtaHisto.Fill(ewBoson2Eta)
  if isLepton1Charged : chargedLeptonEtaHisto.Fill(lepton1Eta)
  if isLepton2Charged : chargedLeptonEtaHisto.Fill(lepton2Eta)
  if isLepton3Charged : chargedLeptonEtaHisto.Fill(lepton3Eta)
  if isLepton4Charged : chargedLeptonEtaHisto.Fill(lepton4Eta)

  higgsPhiHisto.Fill(higgsPhi)
  ewBosonPhiHisto.Fill(ewBoson1Phi)
  ewBosonPhiHisto.Fill(ewBoson2Phi)
  if isLepton1Charged : chargedLeptonPhiHisto.Fill(lepton1Phi)
  if isLepton2Charged : chargedLeptonPhiHisto.Fill(lepton2Phi)
  if isLepton3Charged : chargedLeptonPhiHisto.Fill(lepton3Phi)
  if isLepton4Charged : chargedLeptonPhiHisto.Fill(lepton4Phi)


canvas = TCanvas("c1", "canvas")

canvas.SetWindowSize(1024, 768)

# pt stuff

canvas.SetLogy()
higgsPtHisto.Draw()
higgsPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_higgsPtHisto.png", "png")
canvas.Print(argv[1] + "_higgsPtHisto.svg", "svg")
ewBosonPtHisto.Draw()
ewBosonPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_EWBosonPtHisto.png", "png")
canvas.Print(argv[1] + "_EWBosonPtHisto.svg", "svg")
ewBosonLeadingPtHisto.Draw()
ewBosonLeadingPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_EWLeadingPtHisto.png", "png")
canvas.Print(argv[1] + "_EWLeadingPtHisto.svg", "svg")
ewBosonSubLeadingPtHisto.Draw()
ewBosonSubLeadingPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_EWSubLeadingPtHisto.png", "png")
canvas.Print(argv[1] + "_EWSubLeadingPtHisto.svg", "svg")
chargedLeptonPtHisto.Draw()
chargedLeptonPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_ChargedLeptonsPtHisto.png", "png")
canvas.Print(argv[1] + "_ChargedLeptonsPtHisto.svg", "svg")
neutralLeptonPtHisto.Draw()
neutralLeptonPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_NeutralLeptonsPtHisto.png", "png")
canvas.Print(argv[1] + "_NeutralLeptonsPtHisto.svg", "svg")


# EW Boson 1 + EW Boson 2 + total distribution
ewBoson1PtHisto.SetLineColor(2)
ewBoson2PtHisto.SetLineColor(3)
ewBosonPtHisto.Draw()
ewBosonPtHisto.Write()
ewBoson1PtHisto.Draw("SAME")
ewBoson1PtHisto.Write()
ewBoson2PtHisto.Draw("SAME")
ewBoson2PtHisto.Write()
leg1 = TLegend(0.7,0.7,0.48,0.9)
leg1.SetHeader("Momentum distribution")
leg1.AddEntry(ewBosonPtHisto,"EW boson 1 + EW Boson 2","l")
leg1.AddEntry(ewBoson1PtHisto,"EW Boson 1","l")
leg1.AddEntry(ewBoson2PtHisto,"EW Boson 2","l")
leg1.Draw()
canvas.Update()
canvas.Print(argv[1] + "_EWBosonPtHistogramComparison_1.png", "png")
canvas.Print(argv[1] + "_EWBosonPtHistogramComparison_1.svg", "svg")

# Leading + sub-leading + total distribution
ewBosonLeadingPtHisto.SetLineColor(2)
ewBosonSubLeadingPtHisto.SetLineColor(3)
ewBosonPtHisto.Draw()
ewBosonPtHisto.Write()
ewBosonLeadingPtHisto.Draw("SAME")
ewBosonLeadingPtHisto.Write()
ewBosonSubLeadingPtHisto.Draw("SAME")
ewBosonSubLeadingPtHisto.Write()
leg2 = TLegend(0.7,0.7,0.48,0.9)
leg2.SetHeader("Momentum distribution")
leg2.AddEntry(ewBosonPtHisto,"Leading+sub-leading","l")
leg2.AddEntry(ewBosonLeadingPtHisto,"Leading pt","l")
leg2.AddEntry(ewBosonSubLeadingPtHisto,"Sub-leading pt","l")
leg2.Draw()
canvas.Update()
canvas.Print(argv[1] + "_EWBosonPtHistogramComparison_2.png", "png")
canvas.Print(argv[1] + "_EWBosonPtHistogramComparison_2.svg", "svg")

# Pt of the four leptons
lepton2PtHisto.SetLineColor(2)
lepton3PtHisto.SetLineColor(3)
lepton4PtHisto.SetLineColor(6)
lepton1PtHisto.Draw()
lepton1PtHisto.Write()
lepton2PtHisto.Draw("SAME")
lepton2PtHisto.Write()
lepton3PtHisto.Draw("SAME")
lepton3PtHisto.Write()
lepton4PtHisto.Draw("SAME")
lepton4PtHisto.Write()
leg3 = TLegend(0.7,0.7,0.48,0.9)
leg3.SetHeader("Momentum distribution")
leg3.AddEntry(lepton1PtHisto,"Lepton 1","l")
leg3.AddEntry(lepton2PtHisto,"Lepton 2","l")
leg3.AddEntry(lepton3PtHisto,"Lepton 3","l")
leg3.AddEntry(lepton4PtHisto,"Lepton 4","l")
leg3.Draw()
canvas.Update()
canvas.Print(argv[1] + "_LeptonPtHistogramComparison.png", "png")
canvas.Print(argv[1] + "_LeptonPtHistogramComparison.svg", "svg")

leadingChargedLeptonPtHisto.Draw()
leadingChargedLeptonPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_LeadingChargedLeptonPtHisto.png", "png")
canvas.Print(argv[1] + "_LeadingChargedLeptonPtHisto.svg", "svg")
chargedLeptonLeadingEtaHisto.Draw()
chargedLeptonLeadingEtaHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_LeadingChargedLeptonEtaHisto.png", "png")
canvas.Print(argv[1] + "_LeadingChargedLeptonEtaHisto.svg", "svg")

# Eta distributions
higgsEtaHisto.Draw()
higgsEtaHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_higgsEtaHisto.png", "png")
canvas.Print(argv[1] + "_higgsEtaHisto.svg", "svg")
ewBosonEtaHisto.Draw()
ewBosonEtaHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_decayEtaHisto.png", "png")
canvas.Print(argv[1] + "_decayEtaHisto.svg", "svg")
chargedLeptonEtaHisto.Draw()
chargedLeptonEtaHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_ChargedLeptonEtaHisto.png", "png")
canvas.Print(argv[1] + "_ChargedLeptonEtaHisto.svg", "svg")

# Phi distributions
higgsPhiHisto.Draw()
higgsPhiHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_higgsPhiHisto.png", "png")
canvas.Print(argv[1] + "_higgsPhiHisto.svg", "svg")
ewBosonPhiHisto.Draw()
ewBosonPhiHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_decayPhiHisto.png", "png")
canvas.Print(argv[1] + "_decayPhiHisto.svg", "svg")
chargedLeptonPhiHisto.Draw()
chargedLeptonPhiHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_ChargedLeptonPhiHisto.png", "png")
canvas.Print(argv[1] + "_ChargedLeptonPhiHisto.svg", "svg")

outputFile.Close()