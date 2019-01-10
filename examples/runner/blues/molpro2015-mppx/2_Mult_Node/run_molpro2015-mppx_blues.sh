#!/bin/sh

# Set current working directory
CWD=/blues/gpfs/home/kmoore/elstruct-interface/examples/runner/blues/molpro2015-mppx/2_Mult_Node

# Set host
HOST=b440,b441

# Load Molpro 
soft add +molpro-2015.1-mvapich2
MOLPROEXE=$(which molpro.exe)

# Load intel and MPI libraries
soft add +mvapich2-2.2b-intel-15.0
soft add +intel-15.0
soft add +libpciaccess-0.13.4
soft add +libxml2-2.9.4

# Load GCC library 
soft add +gcc-4.7.2

# Set Molpro library directory
MOLPRO_LIB=/soft/molpro/2015.1_mvapich2/lib/

# Set the Molpro scratch directory
SCRDIR=/scratch/$USER

# Set runtime options for MPI
MPI_OPTIONS="-n 16 -ppn 8 -hosts $HOST"

# Set runtime options for Molpro
MOLPRO_OPTIONS="--mppx --nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $SCRDIR -I $SCRDIR -W $SCRDIR -o $CWD/output.dat"

# Run the molpro executable
mpirun $MPI_OPTIONS $MOLPROEXE $MOLPRO_OPTIONS $CWD/input.dat &


