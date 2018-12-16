#!/bin/bash

# Set current working directory
CWD=$(pwd)

# Run Psi4
% if background == 'yes':
psi4 -n ${ncores_per_nodes} -i $CWD/${input} -o $CWD/${output} &
% else:
psi4 -n ${ncores_per_nodes} -i $CWD/${input} -o $CWD/${output} 
% endif

