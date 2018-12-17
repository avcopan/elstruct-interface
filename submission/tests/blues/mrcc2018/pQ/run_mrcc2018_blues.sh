#!/bin/bash

# Set path
CWD=$(pwd)

# Set host node to the one specified by the user
HOST=b460

# Add executables for executable
export PATH=/lcrc/project/PACC/brossdh/mrcc_blues:$PATH
MRCCEXE=$(which dmrcc)

# Set num threads for OpenMP
export OMP_NUM_THREADS=8

# Create the scratch irectory
export TMPDIR=/scratch/$USER

# SSH into node
ssh -n $HOST " soft add +intel-parallel-studio-17.0.4  ;
               export PATH=$PATH                       ;
               export OMP_NUM_THREADS=$OMP_NUM_THREADS ;
               mkdir -p $TMPDIR                        ;
               cp $CWD/input.dat $TMPDIR/MINP           ;
               cd $TMPDIR                              ;
               $MRCCEXE >& $CWD/output.dat               " &


