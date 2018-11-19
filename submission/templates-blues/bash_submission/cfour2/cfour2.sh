#!/bin/bash

echo "Setting runtime variables and loading necesary libraries" >> $PWD/job_status

# Add CFOUR executables to PATH and set full path to Orca executable to have access to all Orca binaries at runtime
export PATH=$PATH:/lcrc/project/PACC/brossdh/cfour/bin/
CFOUREXE=$(which xcfour)
CFOURXJA=$(which xja2fja)
CFOURBASIS=/lcrc/project/PACC/brossdh/cfour/basis/

# Load Intel parallel studio 
module load intel-parallel-studio/cluster.2018.1-egcacag

# Set variables for parallelization 
nproc=`grep -c ^processor /proc/cpuinfo`
export CFOUR_NUM_CORES=8
export OMP_NUM_THREADS=`echo 'scale=0;'$nproc'/'$CFOUR_NUM_CORES | bc`

echo "Creating scratch directory" >> $PWD/job_status.log

# Set the scratch and current working directory
export TMPDIR=/scratch/$USER
mkdir -p $TMPDIR

echo "Copying the input file to node" >> $PWD/job_status.log
echo "Copying files containing guesses for the geometry, orbitals, and Hessian, if available" >> $PWD/job_status.log

# Copy file from scratch
cp $PWD/ZMAT $TMPDIR/ZMAT

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

echo "Running CFOUR 2.0" >> job_status.log

# Run CFOUR 
$CFOUREXE > $PWD/output.dat &
$CFOURXJA &

echo "Copying additional useful job information to working directory" >> job_status.log

# Place other useful job info in a separate directory 
mkdir -p $PWD/Job_Data
cp $TMPDIR/den.dat  $PWD/Job_Data/den.dat 
cp $TMPDIR/FCMINT   $PWD/Job_Data/FCMINT
cp $TMPDIR/FCMFINAL $PWD/Job_Data/FCMFINAL 
cp $TMPDIR/JOBARC   $PWD/Job_Data/JOBARC
cp $TMPDIR/JAINDX   $PWD/Job_Data/JAINDX 
cp $TMPDIR/MOLDEN   $PWD/Job_Data/MOLDEN 
cp $TMPDIR/ZMATnew  $PWD/ZMATnew 
if [ -e "$TMPDIR/zmat001" ]; then mkdir $PWD/Disps ; cp $TMPDIR/zmat* $PWD/Disps ; fi
if [ -e "$TMPDIR/FJOBARC"  ]; then cp $TMPDIR/FJOBARC $PWD/Job_Data/FJOBARC                   ; fi

# Go back to working directory
cd $PWD

echo "Deleting the scratch directory" >> job_status.log
echo "Job completion" >> job_status

