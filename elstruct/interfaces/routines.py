import importlib

PROGS = ('g09', 'molpro', 'psi4')


def energy(prog, runner, theory, basis, labels, coords, charge=0, mult=1,
           niter=100, thresh_log=12):
    assert prog in PROGS
    prog_name = '.{:s}'.format(prog)
    package = 'elstruct.interfaces'
    mod = importlib.import_module(prog_name, package)
    return mod.energy.energy(runner, theory, basis, labels, coords, charge,
            mult, niter, thresh_log)
