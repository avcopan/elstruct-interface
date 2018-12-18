import numpy
import elstruct


# Runtime
HOSTNODES = 'b451'
NCORES_PER_NODE = 4

# Assign variables to build input string
BASIS = 'cc-pVDZ'
CHARGE = 0
MULT = 1
LABELS = ('O', 'H', 'H')
COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
          (0.000000000000,  1.638036840407,  1.136548822547),
          (0.000000000000, -1.638036840407,  1.136548822547))

def test__psi4_energy():
      
    THEORIES = ['rhf', 'ccsd']
    for THEORY in THEORIES:

      # Obtain input string using the writer function
      INPUT_STR = elstruct.writer.psi4.energy(
          theory=THEORY, basis=BASIS, labels=LABELS, coords=COORDS,
          charge=CHARGE, mult=MULT)

      # Write input file to file
      with open('input.dat', 'w') as inp_fle: inp_fle.write(INPUT_STR)

      # User the runner function to submit psi4 job to Blues/Bebop
      elstruct.runner.blues.submit(program='psi4', hostnodes=HOSTNODES, ncores_per_node=NCORES_PER_NODE)

      # Obtain output string that would be passed to reader function
      with open('output.dat') as out_file: OUTPUT_STR = out_file.read()

      # User energy reader function to get the single point energy
      ENERGY = elstruct.reader.psi4.energy(
            theory=THEORY, output=OUTPUT_STR)

      # Print energy to screen
      if THEORY == 'rhf':
          ecomp = -75.545728027289
      elif THEORY == 'ccsd':
          ecomp = -75.9111895443
      assert numpy.isclose(ENERGY, ecomp, atol=1e-3)


def test__molpro_energy():
    
    THEORIES = ['rhf', 'ccsd']
    for THEORY in THEORIES:

      # Obtain input string using the writer function
      INPUT_STR = elstruct.writer.molpro.energy(
          theory=THEORY, basis=BASIS, labels=LABELS, coords=COORDS,
          charge=CHARGE, mult=MULT)

      # Write input file to file
      with open('input.dat', 'w') as inp_fle: inp_fle.write(INPUT_STR)

      # User the runner function to submit psi4 job to Blues/Bebop
      elstruct.runner.blues.submit(program='molpro2015', hostnodes=HOSTNODES, ncores_per_node=NCORES_PER_NODE)

      # Obtain output string that would be passed to reader function
      with open('output.dat') as out_file: OUTPUT_STR = out_file.read()

      # User energy reader function to get the single point energy
      ENERGY = elstruct.reader.molpro.energy(
            theory=THEORY, output=OUTPUT_STR)

      # Print energy to screen
      if THEORY == 'rhf':
          ecomp = -75.545728027289
      elif THEORY == 'ccsd':
          ecomp = -75.9111895443
      assert numpy.isclose(ENERGY, ecomp, atol=1e-3)


if __name__ == '__main__':
    test__psi4_energy()
    test__molpro_energy()
