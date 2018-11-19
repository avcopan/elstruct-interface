#!/bin/sh

HOST=${hostnodes}

ssh -n $HOST << EOF

export PATH=$PATH:/soft/orca/orca_4_0_1_2_linux_x86-64_openmpi202/
ORCAEXE=$(which orca)

export PATH=/soft/spack-0.10.0/opt/spack/linux-centos6-x86_64/intel-17.0.2/openmpi-2.0.2-pyxkvzeiklfv4v67y46xheicu5j2no4v/bin:$PATH
export LD_LIBRARY_PATH=/soft/spack-0.10.0/opt/spack/linux-centos6-x86_64/intel-17.0.2/openmpi-2.0.2-pyxkvzeiklfv4v67y46xheicu5j2no4v/lib:$LD_LIBRARY_PATH

export TMPDIR=/scratch/$USER
mkdir -p $TMPDIR

cp $PWD/input.dat $TMPDIR/input.dat

if [ -e $PWD/input.xyz  ]; then cp $PWD/input.xyz  $TMPDIR/guess.xyz  ; fi 
if [ -e $PWD/input.gbw  ]; then cp $PWD/input.gbw  $TMPDIR/guess.gbw  ; fi 
if [ -e $PWD/input.hess ]; then cp $PWD/input.hess $TMPDIR/guess.hess ; fi 
if [ -e $PWD/input.pot  ]; then cp $PWD/input.pot  $TMPDIR/guess.pot  ; fi 

$ORCAEXE $TMPDIR/input.dat > $PWD/output.dat

mkdir -p $PWD/Job_Data
cp $TMPDIR/*.xyz  $PWD/Job_Data 
cp $TMPDIR/*.gbw  $PWD/Job_Data 
cp $TMPDIR/*.hess $PWD/Job_Data 
cp $TMPDIR/*.pot  $PWD/Job_Data 

EOF

