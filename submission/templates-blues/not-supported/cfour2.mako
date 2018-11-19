#!/bin/bash

echo "Setting job to run on Blues node(s): ${hostnodes}" >> $PWD/job_status.log

# Set host node to the one specified by the user
HOST=${hostnodes}

# SSH into the Blues node (b4xx) while feeding as series of commands:
# Add CFOUR executables to PATH and set full path to Orca executable to have access to all Orca binaries at runtime
# Load Intel parallel studio 
# Set variables for parallelization 
# Set the scratch and current working directory
# Copy file from scratch

ssh $HOST << EOF

echo "Setting runtime variables and loading necesary libraries"

export PATH=$PATH:/lcrc/project/PACC/brossdh/cfour/bin/
CFOUREXE=$(which xcfour)
CFOURBASIS=/lcrc/project/PACC/brossdh/cfour/basis/

module load intel-parallel-studio/cluster.2018.1-egcacag

nproc=`grep -c ^processor /proc/cpuinfo`
export CFOUR_NUM_CORES=$SLURM_NTASKS
export OMP_NUM_THREADS=`echo 'scale=0;'$nproc'/'$CFOUR_NUM_CORES | bc`

export TMPDIR=/scratch/$USER
mkdir -p $TMPDIR

echo "Copying the input file to node" >> $PWD/
echo "Copying files containing guesses for the geometry, orbitals, and Hessian, if available"

# Copy file from scratch
cp $PWD/${input} $TMPDIR/ZMAT

# Copy files with the basis set and ECP, checking first if one is in working dir 
if [ -e $PWD/GENBAS   ]; then 
  cp $PWD/GENBAS  $TMPDIR/GENBAS 
else
  cp $CFOURBASIS/GENBAS  $TMPDIR/GENBAS 
fi 

if [ -e $PWD/ECPDATA  ]; then 
  cp $PWD/ECPDATA  $TMPDIR/ECPDATA 
else
  cp $CFOURBASIS/ECPDATA  $TMPDIR/ECPDATA
fi 

# Copy files with guess orbitals, Hessian 
if [ -e $PWD/initden.dat  ]; then cp $PWD/initden.dat  $TMPDIR/initden.dat  ; fi 
if [ -e $PWD/FCMINT       ]; then cp $PWD/FCMINT       $TMPDIR/FCMINT       ; fi 

# Change into scratch directory
cd $TMPDIR

echo "Running CFOUR 2.0"

# Run CFOUR 
$CFOUREXE >& $PWD/${output}

echo "Copying additional useful job information to working directory"

# Place other useful job info in a separate directory 
mkdir -p $PWD/Job_Data
cp $TMPDIR/den.dat  $PWD/Job_Data/den.dat 
cp $TMPDIR/FCMINT   $PWD/Job_Data/FCMINT
cp $TMPDIR/FCMFINAL $PWD/Job_Data/FCMFINAL 
cp $TMPDIR/JOBARC   $PWD/Job_Data/JOBARC
cp $TMPDIR/JAINDX   $PWD/Job_Data/JAINDX 
cp $TMPDIR/MOLDEN   $PWD/Job_Data/MOLDEN 

# Go back to working directory
cd $PWD

echo "Deleting the scratch directory"
echo "Job completion"
 
EOF

