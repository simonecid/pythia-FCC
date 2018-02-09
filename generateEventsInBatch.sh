#!/bin/bash
# Needs around 7 GB

while getopts "j:c:p:c:n:" o; do
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
    c)
      cmdFileName=${OPTARG}
      ;;
    n)
      numEvents=${OPTARG}
      ;;
    esac
done

# cmdFileName = "/software/sb17498/pythia8223/pythia-FCC/minBias_14TeV.cmnd"

HOMEFOLDER="$(pwd)"

source /software/sb17498/FCCSW/init.sh

set -o xtrace
/software/sb17498/pythia8223/pythia-FCC/generateEventsToHepMC.exe -c ${cmdFileName} -o ${HOMEFOLDER}/${jobName}_${clusterId}.${processId}.hepmc -s ${processId} -n ${numEvents}

git clone https://www.github.com/simonecid/delphes

cd /software/sb17498/Delphes_install

./bin/hepmc2pileup ${jobName}_${clusterId}.${processId}.pileup ${jobName}_${clusterId}.${processId}.hepmc


/usr/bin/hdfs dfs -mkdir -p /FCC-hh/${jobName}
/usr/bin/hdfs dfs -moveFromLocal ${jobName}_${clusterId}.${processId}.pileup /FCC-hh/${jobName}/
set +o xtrace