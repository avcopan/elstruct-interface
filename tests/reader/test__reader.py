""" Test readers
"""
import os
import yaml
import numpy
from elstruct import reader

DATA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')


def test__energy():
    """ test reader.energy
    """
    for prog in reader.energy_programs():
        directory_path = os.path.join(DATA_PATH, 'energy', prog)

        reference_path = os.path.join(directory_path, 'reference.yml')

        with open(reference_path) as reference_file:
            reference_energies = yaml.load(reference_file)

        for method in reader.energy_program_methods(prog):
            output_path = os.path.join(directory_path, method + '.out')

            with open(output_path) as output_file:
                output_string = output_file.read()
            energy = reader.energy(prog=prog, method=method, output_string=output_string)
            assert energy == reference_energies[method]


def test__harmonic_frequencies():
    """ test reader.harmonic_frequencies
    """
    for prog in reader.harmonic_frequencies_programs():
        directory_path = os.path.join(DATA_PATH, 'harmonic_frequencies', prog)

        reference_path = os.path.join(directory_path, 'reference.txt')
        reference_harm_freqs = numpy.loadtxt(reference_path)

        output_path = os.path.join(directory_path, 'output.dat')
        with open(output_path) as output_file:
            output_string = output_file.read()

        harm_freqs = reader.harmonic_frequencies(prog=prog, output_string=output_string)

        assert numpy.allclose(harm_freqs, reference_harm_freqs)


if __name__ == '__main__':
    test__energy()
    test__harmonic_frequencies()
