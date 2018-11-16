import elstruct.interfaces.molpro as interface


BASIS = 'STO-3G'
CHARGE = 0
MULT = 1
LABELS = ('O', 'H', 'H')
COORDS = ((0.000000000000,  0.000000000000, -0.143225816552),
          (0.000000000000,  1.638036840407,  1.136548822547),
          (0.000000000000, -1.638036840407,  1.136548822547))
INP_STR = interface.energy.input_string(
        basis=BASIS, labels=LABELS, coords=COORDS, charge=CHARGE, mult=MULT)
print(INP_STR)
