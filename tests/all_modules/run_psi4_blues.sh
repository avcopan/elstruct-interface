#!/bin/bash

# Set current working directory
CWD=$(pwd)

# Run Psi4
psi4 -n 4 -i $CWD/input.dat -o $CWD/output.dat 

