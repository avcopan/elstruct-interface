""" Test readers
"""
import os
from elstruct import reader
import yaml

DATA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')


def test__energy():
    """ test reader.energy
    """
    for prog in reader.energy_programs():
        directory_path = os.path.join(DATA_PATH, prog, 'energy')

        reference_path = os.path.join(directory_path, 'reference.yml')

        with open(reference_path) as reference_file:
            reference_energies = yaml.load(reference_file)

        for method in reader.energy_program_methods(prog):
            output_path = os.path.join(directory_path, method + '.out')

            with open(output_path) as output_file:
                output_string = output_file.read()
            energy = reader.energy(prog=prog, method=method, output_string=output_string)
            assert energy == reference_energies[method]


if __name__ == '__main__':
    test__energy()
