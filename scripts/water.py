import subprocess
import elstruct.interfaces.molpro as interface
from mako.template import Template

# create input
BASIS = 'STO-3G'
CHARGE = 0
MULT = 1
LABELS = ('O', 'H', 'H')
COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
          (0.000000000000,  1.638036840407,  1.136548822547),
          (0.000000000000, -1.638036840407,  1.136548822547))
INP_STR = interface.energy.input_string(
        basis=BASIS, labels=LABELS, coords=COORDS, charge=CHARGE, mult=MULT)

# make the caller
NNODES = 1
NCORES_TOTAL = 4
NCORES_PER_NODE = 4
HOSTNODES = 'b440'
MACHINEFILE = "Null"
INPUT = 'input.dat'
OUTPUT = 'output.dat'
INP_FLE = open(INPUT, 'w')
INP_FLE.write(INP_STR)

fill_vals = {
    'nnodes': NNODES,
    'ncores_total': NCORES_TOTAL,
    'ncores_per_node': NCORES_PER_NODE,
    'hostnodes': HOSTNODES,
    'machinefile': MACHINEFILE,
    'input': INPUT,
    'output': OUTPUT}
TEMP_STR = Template(filename='/lcrc/project/PACC/submission/templates-blues/molpro2015.mako').render(**fill_vals)
TEMP_FLE = open('run.sh', 'w')
TEMP_FLE.write(TEMP_STR)
TEMP_FLE.close()

subprocess.check_call(["chmod", "+x", 'run.sh'])
subprocess.check_call(['./run.sh'])
