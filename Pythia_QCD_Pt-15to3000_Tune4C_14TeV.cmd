!
! File: Pythia_minBias.cmd
!
! This file contains commands to be read in for a Pythia8 run.
! Lines not beginning with a letter or digit are comments.
! Names are case-insensitive  -  but spellings-sensitive!
! Adjusted from Pythia example: main03.cmnd.

! 1) Settings used in the main program.
Main:numberOfEvents = 100          ! number of events to generate

! 2) Settings related to output in init(), next() and stat() functions.
Init:showChangedSettings = on      ! list changed settings
Init:showChangedParticleData = off ! list changed particle data
Next:numberCount = 10              ! print message every n events
Next:numberShowInfo = 1            ! print event information n times
Next:numberShowProcess = 1         ! print process record n times
Next:numberShowEvent = 0           ! print event record n times

! 3) Beam parameter settings. Values below agree with default ones.
Beams:idA = 2212                   ! first beam, p = 2212, pbar = -2212
Beams:idB = 2212                   ! second beam, p = 2212, pbar = -2212
Beams:eCM = 14000.                ! CM energy of collision in GeV

! Example b): t-tbar production.
#Top:gg2ttbar = on                 ! g g -> t tbar
#Top:qqbar2ttbar = on              ! q qbar -> t tbar

! Example c): Z0 production; should set mMin.
#WeakSingleBoson:ffbar2gmZ = on    ! q qbar -> gamma*/Z0
#PhaseSpace:mHatMin = 50.

! Example d): gauge boson pair production; set pTmin. Not yet complete.
#WeakDoubleBoson:ffbar2ZW = on     ! q qbar -> Z0 W+-
#WeakDoubleBoson:ffbar2WW = on     ! q qbar -> W+ W-
#PhaseSpace:pTHatMin = 20.         ! minimal pT scale in process

! 5) Switch on/off the key event generation steps.
#PartonLevel:MPI = off             ! no multiparton interactions
#PartonLevel:ISR = off             ! no initial-state radiation
#PartonLevel:FSR = off             ! no final-state radiation
#HadronLevel:Hadronize = off       ! no hadronization
#HadronLevel:Decay = off           ! no decays

! 6) Random generator
Random:setSeed = on                ! apply user-set seed everytime the Pythia::init is called
Random:seed    = 1                 ! -1=default seed, 0=seed based on time, >0 user seed number 

! 7) Other settings. Can be expanded as desired.
#Tune:preferLHAPDF = off           ! use internal PDFs when LHAPDF not linked
ParticleDecays:limitCylinder = on
ParticleDecays:xyMax = 20          ! mm
ParticleDecays:zMax = 30000        ! mm, (full extent of beampipe)

Main:timesAllowErrors    = 10000
ParticleDecays:limitTau0 = on
ParticleDecays:tauMax = 10
HardQCD:all = on
PhaseSpace:pTHatMin = 15
PhaseSpace:pTHatMax = 3000
PhaseSpace:bias2Selection = on
PhaseSpace:bias2SelectionPow = 4.5
PhaseSpace:bias2SelectionRef = 15.
Tune:pp 5
Tune:ee 3

BeamRemnants:halfScaleForKT = 1.00000 
BeamRemnants:primordialKThard = 2.00000 
BeamRemnants:primordialKTsoft = 0.50000 
ColourReconnection:range = 1.50000 
Diffraction:largeMassSuppress = 2.00000 
HardQCD:all = on 
Main:timesAllowErrors = 10000 
MultipartonInteractions:alphaSvalue = 0.13500 
MultipartonInteractions:ecmPow = 0.19000 
MultipartonInteractions:ecmRef = 1800.000 
MultipartonInteractions:expPow = 2.00000 
MultipartonInteractions:pT0Ref = 2.08500 
Next:numberShowEvent = 0 
ParticleDecays:limitTau0 = on 
PDF:pSet = 8 
PhaseSpace:bias2Selection = on 
PhaseSpace:bias2SelectionPow = 4.50000 
PhaseSpace:bias2SelectionRef = 15.00000 
PhaseSpace:pTHatMax = 3000.000 
PhaseSpace:pTHatMin = 15.00000 
SigmaProcess:alphaSvalue = 0.13500 
SpaceShower:alphaSvalue = 0.13700 
SpaceShower:ecmRef = 1800.000 
StringFlav:etaSup = 0.63000 
StringFlav:mesonBvector = 3.00000 
StringFlav:mesonCvector = 1.06000 
StringFlav:mesonSvector = 0.72500 
StringFlav:mesonUDvector = 0.62000 
StringFlav:popcornSpair = 0.50000 
StringFlav:probQQ1toQQ0 = 0.0270000 
StringFlav:probQQtoQ = 0.0900000 
StringFlav:probSQtoQQ = 1.00000 
StringFlav:probStoUD = 0.19000 
StringPT:sigma = 0.30400 
StringZ:aExtraDiquark = 0.50000 
StringZ:aLund = 0.30000 
StringZ:bLund = 0.80000 
StringZ:rFactB = 0.67000 
StringZ:rFactC = 1.00000 
TimeShower:alphaSvalue = 0.13830 
TimeShower:pTmin = 0.40000 
TimeShower:pTminChgQ = 0.40000 
Tune:ee = 3 
Tune:pp = 5 