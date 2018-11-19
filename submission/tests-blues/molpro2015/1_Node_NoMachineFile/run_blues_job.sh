#!/bin/sh

echo "Setting runtime variables and loading necesary libraries" >> job_status.log

# Load Molpro 
soft add +molpro-2015.1-mvapich2

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

echo "Settting MPI options" >> job_status.log

# Set runtime options for MPI
MPI_OPTIONS="-n 4 -ppn 4 -hosts b437"

echo "Settting Molpro options" >> job_status.log

# Set runtime options for Molpro
MOLPRO_OPTIONS="--nouse-logfile --no-xml-output -L $MOLPRO_LIB -d $TMPDIR -I $TMPDIR -W $TMPDIR -o output.dat"

echo "Creating scratch directory" >> job_status.log
echo "Running Molpro2015" >> job_status.log

# Run the molpro executable
mpirun $MPI_OPTIONS molpro.exe $MOLPRO_OPTIONS input.dat &

echo "Deleting scratch directory" >> job_status.log

# Remove scratch directory
rm -rf $TMPDIR

echo "Job completion" >> job_status.log

