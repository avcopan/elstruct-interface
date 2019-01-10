""" common parameters
"""

class METHOD():
    # Ab initio electronic structure methods
    RHF      = 'rhf'
    UHF      = 'uhf'
    MP2      = 'mp2'
    RHF_MP2  = 'rhf-mp2'
    UHF_MP2  = 'uhf-mp2'
    RHF_RMP2 = 'rhf-rmp2'
    RHF_CCSD = 'rhf-ccsd'
    RHF_RCCSD = 'rhf-rccsd'
    RHF_CCSD_T  = 'rhf-ccsd(t)'
    RHF_RCCSD_T = 'rhf-rccsd(t)'
    CASSCF   = 'casscf'
    CASPT2   = 'caspt2'
    icCASPT2 = 'iccaspt2'
    MRCISD_Q = 'mrcisd+q'
    CUSTOM   = 'custom'


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


