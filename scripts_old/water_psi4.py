import subprocess
import elstruct_old.interfaces as interfaces
from mako.template import Template

PROG = 'psi4'
THEORY = 'rhf'

# create input
BASIS = 'STO-3G'
CHARGE = 1
MULT = 2
LABELS = ('O', 'H', 'H')
COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
          (0.000000000000,  1.638036840407,  1.136548822547),
          (0.000000000000, -1.638036840407,  1.136548822547))

# make the caller
def runner(inp_str):
    with open('input.dat', 'w') as inp_fle:
        inp_fle.write(inp_str)

    subprocess.check_call(["psi4", "-i", "input.dat", "-o", "output.dat"])

    with open('output.dat') as out_fle:
        out_str = out_fle.read()

    return out_str


ENERGY = interfaces.energy(
        prog=PROG, runner=runner, theory=THEORY, basis=BASIS, labels=LABELS,
        coords=COORDS, charge=CHARGE, mult=MULT)
print(ENERGY)
