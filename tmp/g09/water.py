import subprocess
import elstruct.interfaces as interfaces
from mako.template import Template

PROG = 'g09'
THEORY = 'rhf'

# create input
BASIS = 'STO-3G'
CHARGE = 0
MULT = 1
LABELS = ('O', 'H', 'H')
COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
          (0.000000000000,  1.638036840407,  1.136548822547),
          (0.000000000000, -1.638036840407,  1.136548822547))

fill_vals = {
    'hostnodes': "b440",
    'input': "input.dat",
    'output': "output.dat"
}
TEMP_STR = Template(filename='g09e.mako').render(**fill_vals)

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
