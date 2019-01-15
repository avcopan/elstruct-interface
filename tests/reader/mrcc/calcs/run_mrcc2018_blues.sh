#!/bin/bash

# Set path
CWD=/blues/gpfs/home/kmoore/elstruct-interface/tests/reader/mrcc/calcs

# Set host node to the one specified by the user
HOST=b450

# Add executables for executable
export PATH=/lcrc/project/PACC/brossdh/mrcc_blues:$PATH
MRCCEXE=$(which dmrcc)

# Set num threads for OpenMP
export OMP_NUM_THREADS=1

# Create the scratch irectory
export TMPDIR=/scratch/$USER
timestamp=$(date +%s%9N)
export SCRDIR=$TMPDIR/MRCCSCR_$timestamp

# SSH into node
ssh -n $HOST " soft add +intel-parallel-studio-17.0.4                            ;
               export PATH=$PATH                                                 ;
               export OMP_NUM_THREADS=$OMP_NUM_THREADS                           ;
               mkdir -p $TMPDIR                                                  ;
               mkdir -p $SCRDIR                                                  ;
               cp $CWD/uhf.inp $SCRDIR/MINP                                     ;
               cd $TMPDIR                                                        ;
               cd $SCRDIR                                                        ;
               $MRCCEXE >& $CWD/uhf.out                                        ;
               cd $TMPDIR                                                        ;
               rm -r MRCCSCR_$timestamp                                          ;
               cd $CWD                                                             " 
