#!/bin/sh

echo "Setting runtime variables and loading necesary libraries" >> $PWD/job_status.log

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
MOLPRO_LIB=/soft/molpro/2015.1_170920/bebop/molprop_2015_1_linux_x86_64_i8/lib/

# Set the Molpro scratch directory
TMPDIR=/scratch/$USER

echo "Settting MPI options" >> $PWD/job_status.log

# Set runtime options for MPI
%if machinefile == "Null":
MPI_OPTIONS="-n ${ncores_total} -ppn ${ncores_per_node} -hosts ${hostnodes}"
%else:
MPI_OPTIONS="-f ${machinefile}"
%endif

echo "Settting Molpro options" >> $PWD/job_status.log

# Set runtime options for Molpro
%if nnodes == 1:
MOLPRO_OPTIONS="--nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o ${output}"
%else:
MOLPRO_OPTIONS="--mppx --nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o ${output}"
%endif

echo "Creating scratch directory" >> $PWD/job_status.log
echo "Running Molpro2015" >> $PWD/job_status.log

# Run the molpro executable
mpirun $MPI_OPTIONS $MOLPROEXE $MOLPRO_OPTIONS $PWD/${input} &

echo "Deleting scratch directory" >> $PWD/job_status.log

# Remove scratch directory
#rm -r $TMPDIR

echo "Job completion" >> $PWD/job_status.log

