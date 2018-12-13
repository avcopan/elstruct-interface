#!/bin/bash

# Set current working directory
CWD=$(pwd)

# Set host
HOST=b450

# Set variables for NWChem
export NWCHEMEXE=/soft/nwchem/bebop/bdw-casper/bin/nwchem 

# Load intel and MPI libraries
soft add +mvapich2-2.2b-intel-15.0
soft add +intel-15.0
soft add +libpciaccess-0.13.4
soft add +libxml2-2.9.4

# Set MPI
export I_MPI_FABRICS=shm:tmi
export I_MPI_OFI_PROVIDER=psm2

# Include Casper library in LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/soft/nwchem/bebop/bdw-casper/lib/libcasper.so:$LD_LIBRARY_PATH

# Set the scratch directory
export TMPDIR=/scratch/$USER

# Set runtime options for MPI
MPI_OPTIONS="-n 4 -ppn 4 -hosts $HOST"

# Run NWCHEM with MPIs
mpirun $MPI_OPTION $NWCHEMEXE $CWD/input.dat > $CWD/output.dat &

