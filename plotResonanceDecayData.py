from ROOT import TFile
from ROOT import TTree
from ROOT import TH1I
from ROOT import TCanvas

myFile = TFile("myFile.root")
tree = myFile.Get("")