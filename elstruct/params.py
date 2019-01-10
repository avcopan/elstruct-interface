""" common parameters
"""

class METHOD():
    # Ab initio electronic structure methods
    RHF      = 'rhf'
    UHF      = 'uhf'
    MP2      = 'mp2'
    RMP2     = 'rmp2'
    UMP2     = 'ump2'
    CCSD     = 'ccsd'
    CCSD(T)  = 'ccsd(t)'
    RCCSD(T) = 'rccsd(t)'
    UCCSD(T) = 'uccsd(t)'
    CASSCF   = 'casscf'
    CASPT2   = 'caspt2'
    icCASPT2 = 'iccaspt2'
    MRCISD_Q = 'mrcisd+q'
    CUSTOM   = 'custom'
    # Density functional theory methods
    B3LYP    = 'B3LYP'
    B2PLYP   = 'B2PLYP'
    WB97X    = 'wB97X'
    M062X    = 'M06-2X'
}


class BASIS():
    # Dunning Correlation Consistent Basis Sets
    PVDZ = 'cc-pvdz'
    PVTZ = 'cc-pvtz'
    PVQZ = 'cc-pvqz'


class PROGRAM():
    # Electronic Structure Programs
    CFOUR = 'cfour2'
    GAUSSIAN = 'gaussian09'
    MOLPRO = 'molpro2015'
    MOLPRO_MPPX = 'molpro2015-mppx'
    MRCC = 'mrcc2018'
    NWCHEM = 'nwchem6'
    ORCA = 'orca4'
    PSI4 = 'psi4'
    QCHEM = 'qchem'


