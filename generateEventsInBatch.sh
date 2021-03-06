#!/bin/bash
# Needs around 7 GB

while getopts "j:c:p:i:n:" o; do
  case "${o}" in
    j)
      jobName=${OPTARG}
      ;;
    c)
      clusterId=${OPTARG}
      ;;
    p)
      processId=${OPTARG}
      ;;  
    i)
      cmdFileName=${OPTARG}
      ;;
    n)
      numEvents=${OPTARG}
      ;;
    esac
done

# cmdFileName = "/software/sb17498/pythia8223/pythia-FCC/minBias_14TeV.cmnd"

HOMEFOLDER="$(pwd)"

source /cvmfs/sft.cern.ch/lcg/contrib/gcc/4.9/x86_64-slc6/setup.sh
source /cvmfs/sft.cern.ch/lcg/releases/ROOT/6.08.06-c8fb4/x86_64-slc6-gcc49-opt/bin/thisroot.sh

set -o xtrace
/software/sb17498/pythia8223/pythia-FCC/generateEventsToHepMC.exe -c ${cmdFileName} -o ${HOMEFOLDER}/${jobName}_${clusterId}.${processId}.hepmc -s ${processId} -n ${numEvents}
set +o xtrace 

source /software/sb17498/FCCSW/init.sh
set -o xtrace
cd /software/sb17498/Delphes_install

./bin/hepmc2pileup ${HOMEFOLDER}/${jobName}_${clusterId}.${processId}.pileup ${HOMEFOLDER}/${jobName}_${clusterId}.${processId}.hepmc


/usr/bin/hdfs dfs -mkdir -p /FCC-hh/${jobName}
/usr/bin/hdfs dfs -moveFromLocal ${HOMEFOLDER}/${jobName}_${clusterId}.${processId}.pileup /FCC-hh/${jobName}/

rm ${HOMEFOLDER}/${jobName}_${clusterId}.${processId}.hepmc
set +o xtrace 