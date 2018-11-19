#!/bin/bash
#SBATCH -p ${partition}
#SBATCH -N 1
#SBATCH --ntasks-per-node=${ncores_per_node}
#SBATCH -t ${walltime}
#SBATCH -J ${jobname}
#SBATCH -A ${account}
#SBATCH -o job_%j.log
#SBATCH -e job_%j.err

echo "Setting runtime variables and loading necesary libraries"

# Add Orca executables to PATH and set full path to Orca executable to have access to all Orca binaries at runtime
export PATH=$PATH:/soft/orca/orca_4_0_1_2_linux_x86-64_openmpi202/
ORCAEXE=$(which orca)

# Load the OpenMPI module
module add openmpi/2.1.1-v23idfv

echo "Creating scratch directory"

# Create the scratch directory
export TMPDIR=/scratch/$USER
mkdir -p $TMPDIR

echo "Copying the input file to node"
echo "Copying files containing guesses for the geometry, orbitals, and Hessian, if available"

# Copy the input file to scratch 
cp $SLURM_SUBMIT_DIR/input.dat $TMPDIR/input.dat

# Copy files with guess geoms, orbitals, Hessian 
if [ -e $SLURM_SUBMIT_DIR/input.xyz  ]; then cp $SLURM_SUBMIT_DIR/input.xyz  $TMPDIR/guess.xyz  ; fi 
if [ -e $SLURM_SUBMIT_DIR/input.gbw  ]; then cp $SLURM_SUBMIT_DIR/input.gbw  $TMPDIR/guess.gbw  ; fi 
if [ -e $SLURM_SUBMIT_DIR/input.hess ]; then cp $SLURM_SUBMIT_DIR/input.hess $TMPDIR/guess.hess ; fi 
if [ -e $SLURM_SUBMIT_DIR/input.pot  ]; then cp $SLURM_SUBMIT_DIR/input.pot  $TMPDIR/guess.pot ; fi 

echo "Running Orca.4.0.1.2"

# Run Orca
$ORCAEXE $TMPDIR/input.dat > $SLURM_SUBMIT_DIR/output.dat

echo "Copying additional useful job information to working directory"
# Place other useful job info in a separate directory 
:mkdir -p $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB_ID
cp $TMPDIR/*.xyz  $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB_ID 
cp $TMPDIR/*.gbw  $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB_ID
cp $TMPDIR/*.hess $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB_ID 
cp $TMPDIR/*.pot  $SLURM_SUBMIT_DIR/Job_Data_$SLURM_JOB_ID

echo "Deleting the scratch directory"
echo "Job completion"

