#!/bin/bash
#SBATCH -p bdwall
#SBATCH -N 1
#SBATCH --ntasks-per-node=8
#SBATCH -t 2:00:00
#SBATCH -J run
#SBATCH -A PACC
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

# Add Orca executables to PATH and set full path to Orca executable to have access to all Orca binaries at runtime
export PATH=$PATH:/soft/orca/orca_4_0_1_2_linux_x86-64_openmpi202/
ORCAEXE=$(which orca)

# Load the OpenMPI module
module add openmpi/2.1.1-v23idfv

# Create the scratch directory
export TMPDIR=/scratch/$USER
mkdir -p $TMPDIR

# Set variable that includes ampersand if run in the background
BACKGROUND=""

# Copy the input file to scratch 
cp $SLURM_SUBMIT_DIR/input.dat $TMPDIR/input.dat

# Copy files with guess geoms, orbitals, Hessian 
if [ -e $SLURM_SUBMIT_DIR/input.xyz  ]; then cp $SLURM_SUBMIT_DIR/input.xyz  $TMPDIR/guess.xyz  ; fi 
if [ -e $SLURM_SUBMIT_DIR/input.gbw  ]; then cp $SLURM_SUBMIT_DIR/input.gbw  $TMPDIR/guess.gbw  ; fi 
if [ -e $SLURM_SUBMIT_DIR/input.hess ]; then cp $SLURM_SUBMIT_DIR/input.hess $TMPDIR/guess.hess ; fi 
if [ -e $SLURM_SUBMIT_DIR/input.pot  ]; then cp $SLURM_SUBMIT_DIR/input.pot  $TMPDIR/guess.pot  ; fi 

# Run Orca
$ORCAEXE $TMPDIR/input.dat > $SLURM_SUBMIT_DIR/output.dat 

# Place other useful job info in a separate directory 
mkdir -p $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB
cp $TMPDIR/*.xyz  $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB 
cp $TMPDIR/*.gbw  $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB
cp $TMPDIR/*.hess $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB 
cp $TMPDIR/*.pot  $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB

