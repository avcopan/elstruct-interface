import importlib

PROGS = ('g09', 'molpro', 'psi4')

INP_NAME = 'input.dat'
OUT_NAME = 'output.dat'


def energy(prog, runner, theory, basis, labels, coords, charge=0, mult=1,
           niter=100, thresh_log=12):
    assert prog in PROGS
    prog_name = '.{:s}'.format(prog)
    package = 'elstruct.interfaces'
    mod = importlib.import_module(prog_name, package)

    inp_str = mod.energy.input_string(
            theory, basis, labels, coords, charge, mult, niter, thresh_log)
    with open(INP_NAME, 'w') as inp_fle:
        inp_fle.write(inp_str)

    runner()

    with open(OUT_NAME) as out_fle:
        out_str = out_fle.read()

    return mod.energy.read_energy(out_str, theory, basis)
