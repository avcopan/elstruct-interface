import subprocess
import elstruct.interfaces as interfaces
from mako.template import Template

PROG = 'molpro'
THEORY = 'ccsd'

# create input
BASIS = '6-31g'
CHARGE = 1
MULT = 2
LABELS = ('O', 'H', 'H')
COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
          (0.000000000000,  1.638036840407,  1.136548822547),
          (0.000000000000, -1.638036840407,  1.136548822547))

FILL_VALS = {
    'nnodes': 1,
    'ncores_total': 4,
    'ncores_per_node': 4,
    'hostnodes': 'b440',
    'machinefile': "Null",
    'input': 'input.dat',
    'output': 'output.dat'}
TEMP_STR = Template(filename='molpro2015.mako').render(**FILL_VALS)

# make the caller
def runner():
    temp_fle = open('run.sh', 'w')
    temp_fle.write(TEMP_STR)
    temp_fle.close()

    subprocess.check_call(["chmod", "+x", 'run.sh'])
    subprocess.check_call(['./run.sh'])

ENERGY = interfaces.energy(
        prog=PROG, runner=runner, theory=THEORY, basis=BASIS, labels=LABELS,
        coords=COORDS, charge=CHARGE, mult=MULT)
print(ENERGY)
