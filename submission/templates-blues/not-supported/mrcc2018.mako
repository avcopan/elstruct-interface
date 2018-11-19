#!/bin/sh

echo "Setting job to run on Blues node(s): ${hostnodes}" >> $PWD/job_status.log

# Set host node to the one specified by the user
HOST=${hostnodes}

# SSH into the Blues node (b4xx) and feed in command line to run on node
#  (1) Add executables for executable
#  (2) Load the paths for intel-parallel studio
#  (3) Set num threads for OMP
#  (4) Make scratch directory
#  (5) calls MRCC executable on "MINP" file (must have this name) while setting approprate scratch
#  (6) Removes scratch directory
ssh -n $HOST << EOF  

echo "Setting runtime variables and loading necesary libraries" >> $PWD/job_status.log

export PATH=$PATH:/lcrc/project/PACC/brossdh/mrcc/
MRCCEXE=$(which dmrcc)

PATH=/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/advisor_2018.1.1.535164/bin64:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/inspector_2018.1.1.535159/bin64:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/bin/intel64:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/mpi/intel64/bin:$PATH

LD_LIBRARY_PATH=/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/compiler/lib/intel64:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/compiler/lib/intel64_lin:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/mpi/intel64/lib:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/mpi/mic/lib:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/ipp/lib/intel64:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/mkl/lib/intel64_lin:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/tbb/lib/intel64/gcc4.7:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/debugger_2018/iga/lib:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/debugger_2018/libipt/intel64/lib:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/daal/lib/intel64_lin:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/compilers_and_libraries_2018.1.163/linux/tbb/lib/intel64_lin/gcc4.4:/blues/gpfs/home/software/spack-0.10.1/opt/spack/linux-centos7-x86_64/gcc-4.8.5/intel-parallel-studio-cluster.2018.1-egcacagjokllneqafnpkfnp4njzklpsk/lib:$LD_LIBRARY_PATH

echo "Setting the number of threads for OMP" >> $PWD/job_status.log

export OMP_NUM_THREADS=${ncores}

echo "Creating scratch directory" >> $PWD/job_status.log

mkdir -p $TMPDIR             

echo "Running MRCC 2018-10-18" >> $PWD/job_status.log

$MRCCEXE >& $PWD/${output}   

EOF

echo "Job completion" >> $PWD/job_status.log


