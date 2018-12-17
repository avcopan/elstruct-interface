import elstruct
import subprocess

# Assign variables to build input string
THEORY = 'ccsd'
BASIS = 'STO-3G'
CHARGE = 1
MULT = 2
LABELS = ('O', 'H', 'H')
COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
          (0.000000000000,  1.638036840407,  1.136548822547),
          (0.000000000000, -1.638036840407,  1.136548822547))

# Obtain input string using the writer function
INPUT_STR = elstruct.writer.psi4.energy(
        theory=THEORY, basis=BASIS, labels=LABELS, coords=COORDS,
        charge=CHARGE, mult=MULT)

# Write input file to file
with open('input.dat', 'w') as inp_fle:
    inp_fle.write(INPUT_STR)

# Assign variables that are passed to the runner function
PROGRAM = 'psi4'
HOSTNODES = 'b451'

# User the runner function to submit psi4 job to Blues/Bebop
elstruct.runner.blues.submit(program=PROGRAM, hostnodes=HOSTNODES)

# Obtain output string that would be passed to reader function
with open('output.dat') as out_fle:
    OUTPUT_STR = out_fle.read()

# User energy reader function to get the single point energy
ENERGY = elstruct.reader.psi4.energy(
        theory=THEORY, output=OUTPUT_STR)

# Print energy to screen
print(ENERGY)
