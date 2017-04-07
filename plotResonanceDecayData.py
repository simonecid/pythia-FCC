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

numberOfEntries = resonanceDecaysTree.GetEntries()

resonancePtHisto = TH1I("resonancePtHisto", "Resonance pt distribution", 100, 0, 500)
decayPtHisto = TH1I("decayPtHisto", "Decay products pt distribution", 100, 0, 500)
decayLeadingPtHisto = TH1I("decayLeadingPtHisto", "Decay product leading pt distribution", 100, 0, 500)
decaySubLeadingPtHisto = TH1I("decaySubLeadingPtHisto", "Decay product sub-leading pt distribution", 100, 0, 500)

resonanceEtaHisto = TH1I("resonanceEtaHisto", "Resonance eta distribution", 100, -10, +10)
decayEtaHisto = TH1I("decayEtaHisto", "Decay products eta distribution", 100, -10, +10)

resonancePhiHisto = TH1I("resonancePhiHisto", "Resonance phi distribution", 110, -3.30, +3.30)
decayPhiHisto = TH1I("decayPhiHisto", "Decay product phi distribution", 110, -3.30, +3.30)

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

  resonancePtHisto.Fill(resonancePt)
  decayPtHisto.Fill(decay1Pt)
  decayPtHisto.Fill(decay2Pt)
  decayLeadingPtHisto.Fill(leadingPt)
  decaySubLeadingPtHisto.Fill(subLeadingPt)

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
canvas.Update()
canvas.Print(argv[1] + "_resonancePtHisto.png", "png")
decayPtHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_decayPtHisto.png", "png")
decayLeadingPtHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_decayLeadingPtHisto.png", "png")
decaySubLeadingPtHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_decaySubLeadingPtHisto.png", "png")

# Leading + sub-leading + total distribution

decayLeadingPtHisto.SetLineColor(2)
decaySubLeadingPtHisto.SetLineColor(3)
decayPtHisto.Draw()
decayLeadingPtHisto.Draw("SAME")
decaySubLeadingPtHisto.Draw("SAME")
leg = TLegend(0.7,0.7,0.48,0.9)
leg.SetHeader("Momentum distribution")
leg.AddEntry(decayPtHisto,"Leading+sub-leading","l")
leg.AddEntry(decayLeadingPtHisto,"Leading pt","l")
leg.AddEntry(decaySubLeadingPtHisto,"Sub-leading pt","l")
leg.Draw()
canvas.Update()
canvas.Print(argv[1] + "_ptHistogramComparison.png", "png")

resonanceEtaHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_resonanceEtaHisto.png", "png")
decayEtaHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_decayEtaHisto.png", "png")

resonancePhiHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_resonancePhiHisto.png", "png")
decayPhiHisto.Draw()
canvas.Update()
canvas.Print(argv[1] + "_decayPhiHisto.png", "png")