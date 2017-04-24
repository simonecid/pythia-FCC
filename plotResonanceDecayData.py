'''Plots various stuff from the resonance to two product decays.
Receives the name of the root file without extension as an input.
'''


from ROOT import TFile
from ROOT import TTree
from ROOT import TH1I
from ROOT import TCanvas
from ROOT import TLegend
from math import sqrt
from math import hypot
from sys import argv

fileName = argv[1]
resonanceFile = TFile(argv[1] + ".root")
resonanceDecaysTree = resonanceFile.Get("resonanceDecays")

outputFile = TFile(argv[1] + "_plots" + ".root", "RECREATE")

numberOfEntries = resonanceDecaysTree.GetEntries()

'''Plot of the pt distribution of the resonance'''
resonancePtHisto = TH1I("resonancePtHisto", "Resonance pt distribution", 100, 0, 500)
'''Plot of both decay products' pt distribution'''
decayPtHisto = TH1I("decayPtHisto", "pt distribution of the decay products", 100, 0, 500)
'''Plot of the leading pt distribution of the charged decay products'''
decayLeadingPtHisto = TH1I("decayLeadingPtHisto", "Leading pt charged decay product distribution", 100, 0, 500)
'''Plot of the sub-leading pt distribution of the charged decay products'''
decaySubLeadingPtHisto = TH1I("decaySubLeadingPtHisto", "Sub-leading pt decay product distribution", 100, 0, 500)
'''Plot of the eta distribution of the resonance'''
resonanceEtaHisto = TH1I("resonanceEtaHisto", "Resonance eta distribution", 100, -10, +10)
'''Plot of the eta distribution of both decay products'''
decayEtaHisto = TH1I("decayEtaHisto", "Decay products eta distribution", 100, -10, +10)
'''Plot of the eta distribution of leading decay product in pt'''
decayLeadingEtaHisto = TH1I("decayLeadingEtaHisto", "Leading decay product eta distribution", 100, -10, +10)
'''Plot of the eta distribution of sub-leading decay product in pt'''
decaySubLeadingEtaHisto = TH1I("decaySubLeadingEtaHisto", "Sub-leading decay product eta distribution", 100, -10, +10)
'''Plot of the phi distribution of the resonance'''
resonancePhiHisto = TH1I("resonancePhiHisto", "Resonance phi distribution", 110, -3.30, +3.30)
'''Plot of the phi distribution of both decay products'''
decayPhiHisto = TH1I("decayPhiHisto", "Decay product phi distribution", 110, -3.30, +3.30)

'''Plot of the distribution of the pt of a decay product'''
decay1PtHisto = TH1I("decay1PtHisto", "Decay product 1 pt distribution", 100, 0, 500)
'''Plot of the distribution of the pt of a decay products'''
decay2PtHisto = TH1I("decay2PtHisto", "Decay product 2 pt distribution", 100, 0, 500)

chargedLeptonsPDGID = [11, 13, 15, -11, -13, -15]
neutralLeptonsPDGID = [12, 14, 16, -12, -14, -16]

for eventIndex in xrange(0, numberOfEntries):
  resonanceDecaysTree.GetEntry(eventIndex)
  
  # Retrieving Pt
  resonancePt = hypot(resonanceDecaysTree.resonancePx, resonanceDecaysTree.resonancePy)
  decay1Pt = hypot(resonanceDecaysTree.decay1Px, resonanceDecaysTree.decay1Py)
  decay2Pt = hypot(resonanceDecaysTree.decay2Px, resonanceDecaysTree.decay2Py)

  # Retrieving PDGID
  decay1PDGID = resonanceDecaysTree.decay1PDGID
  decay2PDGID = resonanceDecaysTree.decay2PDGID

  # Retrieving eta
  resonanceEta = resonanceDecaysTree.resonanceEta
  decay1Eta = resonanceDecaysTree.decay1Eta
  decay2Eta = resonanceDecaysTree.decay2Eta

  # Retrieving phi
  resonancePhi = resonanceDecaysTree.resonancePhi
  decay1Phi = resonanceDecaysTree.decay1Phi
  decay2Phi = resonanceDecaysTree.decay2Phi

  # Checking if charged 
  isDecay1Charged = decay1PDGID in chargedLeptonsPDGID
  isDecay2Charged = decay2PDGID in chargedLeptonsPDGID

  leadingPt = 0
  subLeadingPt = 0

  if isDecay1Charged:
    leadingPt = decay1Pt
    subLeadingPt = 0
    leadingPt_Eta = decay1Eta
    if isDecay2Charged:
      if decay1Pt > decay2Pt :
        leadingPt = decay1Pt
        subLeadingPt = decay2Pt
        leadingPt_Eta = decay1Eta
        subLeadingPt_Eta = decay2Eta
      else :
        leadingPt = decay2Pt
        subLeadingPt = decay1Pt
        leadingPt_Eta = decay2Eta
        subLeadingPt_Eta = decay1Eta
  elif isDecay2Charged:
    leadingPt = decay2Pt
    subLeadingPt = 0
    leadingPt_Eta = decay2Eta

  # Filling the histogram

  resonancePtHisto.Fill(resonancePt)
  decayPtHisto.Fill(decay1Pt)
  decay1PtHisto.Fill(decay1Pt)
  decayPtHisto.Fill(decay2Pt)
  decay2PtHisto.Fill(decay2Pt)
  if leadingPt > 0: 
    decayLeadingPtHisto.Fill(leadingPt)
    decayLeadingEtaHisto.Fill(leadingPt_Eta)
  if subLeadingPt > 0:
    decaySubLeadingPtHisto.Fill(subLeadingPt)
    decaySubLeadingEtaHisto.Fill(subLeadingPt_Eta)
  

  resonanceEtaHisto.Fill(resonanceEta)
  decayEtaHisto.Fill(decay1Eta)
  decayEtaHisto.Fill(decay2Eta)

  resonancePhiHisto.Fill(resonancePhi)
  decayPhiHisto.Fill(decay1Phi)
  decayPhiHisto.Fill(decay2Phi)

canvas = TCanvas("c1", "canvas")

canvas.SetWindowSize(1024, 768)

# pt stuff

canvas.SetLogy()
resonancePtHisto.Draw()
resonancePtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_resonancePtHisto.png", "png")
decayPtHisto.Draw()
decayPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_decayPtHisto.png", "png")
decayLeadingPtHisto.Draw()
decayLeadingPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_decayLeadingPtHisto.png", "png")
decaySubLeadingPtHisto.Draw()
decaySubLeadingPtHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_decaySubLeadingPtHisto.png", "png")

# Leading + sub-leading + total distribution

decayLeadingPtHisto.SetLineColor(2)
decaySubLeadingPtHisto.SetLineColor(3)
decayPtHisto.Draw()
decayPtHisto.Write()
decayLeadingPtHisto.Draw("SAME")
decayLeadingPtHisto.Write()
decaySubLeadingPtHisto.Draw("SAME")
decaySubLeadingPtHisto.Write()
leg1 = TLegend(0.7,0.7,0.48,0.9)
leg1.SetHeader("Momentum distribution")
leg1.AddEntry(decayPtHisto,"Leading+sub-leading","l")
leg1.AddEntry(decayLeadingPtHisto,"Leading pt","l")
leg1.AddEntry(decaySubLeadingPtHisto,"Sub-leading pt","l")
leg1.Draw()
canvas.Update()
canvas.Print(argv[1] + "_ptHistogramComparison_1.png", "png")

# Decay 1 + decay 2

decay1PtHisto.SetLineColor(2)
decay2PtHisto.SetLineColor(3)
decay1PtHisto.Draw("")
decay1PtHisto.Write()
decay2PtHisto.Draw("SAME")
decay2PtHisto.Write()
leg2 = TLegend(0.7,0.7,0.48,0.9)
leg2.SetHeader("Momentum distribution")
leg2.AddEntry(decay1PtHisto,"Decay product 1","l")
leg2.AddEntry(decay2PtHisto,"Decay product 2","l")
leg2.Draw()
canvas.Update()
canvas.Print(argv[1] + "_ptHistogramComparison_2.png", "png")

resonanceEtaHisto.Draw()
resonanceEtaHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_resonanceEtaHisto.png", "png")
decayEtaHisto.Draw()
decayEtaHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_decayEtaHisto.png", "png")
decayLeadingEtaHisto.Draw()
decayLeadingEtaHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_decayLeadingEtaHisto.png", "png")

resonancePhiHisto.Draw()
resonancePhiHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_resonancePhiHisto.png", "png")
decayPhiHisto.Draw()
decayPhiHisto.Write()
canvas.Update()
canvas.Print(argv[1] + "_decayPhiHisto.png", "png")

outputFile.Close()