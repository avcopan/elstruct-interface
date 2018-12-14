import elstruct
import subprocess

THEORY = 'ccsd'
BASIS = 'STO-3G'
CHARGE = 1
MULT = 2
LABELS = ('O', 'H', 'H')
COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
          (0.000000000000,  1.638036840407,  1.136548822547),
          (0.000000000000, -1.638036840407,  1.136548822547))

INPUT_STR = elstruct.writer.psi4.energy(
        theory=THEORY, basis=BASIS, labels=LABELS, coords=COORDS,
        charge=CHARGE, mult=MULT)
print(INPUT_STR)

with open('input.dat', 'w') as inp_fle:
    inp_fle.write(INPUT_STR)
subprocess.check_call(["psi4", "-i", "input.dat", "-o", "output.dat"])
with open('output.dat') as out_fle:
    OUTPUT_STR = out_fle.read()

ENERGY = elstruct.reader.psi4.energy(
        theory=THEORY, output=OUTPUT_STR)
print(ENERGY)
