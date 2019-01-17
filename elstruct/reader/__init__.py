"""
Modules to read information from electronic structure codes
"""
import importlib
from ..params import PROGRAM

PACKAGE = 'elstruct.reader'
PROGRAM_MODULE_NAMES = {
    PROGRAM.MOLPRO: 'molpro',
    PROGRAM.MOLPRO_MPPX: 'molpro',
}

ENERGY_PROGRAMS = (PROGRAM.MOLPRO, PROGRAM.MOLPRO_MPPX)


def _import_module(prog):
    """ import the module for a specific program
    """
    assert prog in PROGRAM_MODULE_NAMES.keys()
    module_name = PROGRAM_MODULE_NAMES[prog]
    module = importlib.import_module('.'+module_name, PACKAGE)
    return module


def energy_programs():
    """ get the list of programs implementing energy readers
    """
    energy_progs = []
    for prog in PROGRAM_MODULE_NAMES.keys():
        module = _import_module(prog)
        if hasattr(module, 'ENERGY_READERS'):
            energy_progs.append(prog)
    return energy_progs


def energy_program_methods(prog):
    """ get the list of energy reader methods for a given program
    """
    assert prog in energy_programs()
    module = _import_module(prog)
    energy_prog_methods = tuple(module.ENERGY_READERS.keys())
    return energy_prog_methods


def energy(prog, method, output_string):
    """ Retrieves the desired electronic energy.
    """
    assert prog in energy_programs()
    assert method in energy_program_methods(prog)
    module = _import_module(prog)
    energy = module.ENERGY_READERS[method](output_string)
    return energy


#def frequency(freq, output_string):
#    """ Retrieves the desired frequency information.
#    """
#
#    assert freq in FREQUENCY_READERS.keys()
#
#    frequency = FREQUENCY_READERS[freq](output_string)
#
#    return frequency
#def structure(struct, output_string):
#    """ Retrieves the desired structural infromation.
#    """
#
#    assert struct in STRUCTURE_READERS.keys()
#
#    struct = STRUCTURE_READERS[struct](output_string)
#
#    return struct
#def surface(surf, output_string):
#    """ Retrieves the desired information regarding the potential energy surface.
#    """
#
#    surf_info = SURFACE_READERS[surf](output_string)
#
#    return surface_info
#def mol_property(prop, output_string):
#    """ Retrieves the desired molecular property.
#    """
#
#    mol_property = PROPERTY_READERS[prop](output_string)
#
#    return mol_property
#def status(output_string):
#    """ Returns the status of a job.
#    """
#
#    # Check if the job completed or if any error messages were printed
#    job_complete = complete_msg_reader(output_string)
#    job_error_str = error_msg_reader(output_string)
#
#    job_status = [complete_status, job_error_str]
#
#    return job_status
