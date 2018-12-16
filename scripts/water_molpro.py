import elstruct
import subprocess

# Assign variables to build input string
THEORY = 'ccsd'
BASIS = '6-31G*'
CHARGE = 0
MULT = 1
LABELS = ('O', 'H', 'H')
COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
          (0.000000000000,  1.638036840407,  1.136548822547),
          (0.000000000000, -1.638036840407,  1.136548822547))

# Obtain input string using the writer function
INPUT_STR = elstruct.writer.molpro.energy(
        theory=THEORY, basis=BASIS, labels=LABELS, coords=COORDS,
        charge=CHARGE, mult=MULT)

# Write input file to file
with open('input.dat', 'w') as inp_fle:
    inp_fle.write(INPUT_STR)

# Assign variables that are passed to the runner function
PROGRAM = 'molpro2015'
HOSTNODES = 'b444'

# User the runner function to submit to Blues/Bebop
elstruct.runner.blues.submit(program=PROGRAM, hostnodes=HOSTNODES)

# Obtain output string that would be passed to reader function
with open('output.dat') as out_fle:
    OUTPUT_STR = out_fle.read()

#print(OUTPUT_STR)


# User energy reader function to get the single point energy
#ENERGY = elstruct.reader.molpro.energy(
#        theory=THEORY, output=OUTPUT_STR)

# Print energy to screen
#print(ENERGY)
