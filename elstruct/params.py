""" common parameters
"""

class METHOD():
    """ Ab initio electronic structure methods
    """
    # Hartree-Fock methods #
    RHF = 'rhf'
    UHF = 'uhf'
    ROHF = 'rohf'
    # Single-reference correlated methods #
    RHF_MP2 = 'rhf-mp2'
    UHF_UMP2 = 'uhf-ump2'
    ROHF_RMP2 = 'rhf-romp2'
    RHF_CCSD = 'rhf-ccsd'
    ROHF_UCCSD = 'rhf-uccsd'
    ROHF_RCCSD = 'rhf-rccsd'
    RHF_CCSD_T = 'rhf-ccsd(t)'
    ROHF_UCCSD_T = 'rohf-uccsd(t)'
    ROHF_RCCSD_T = 'rohf-rccsd(t)'
    # Multireference methods #
    CASSCF = 'casscf'
    CASPT2 = 'caspt2'
    icCASPT2 = 'iccaspt2'
    MRCISD_Q = 'mrcisd+q'
    # Custom, user-defined method #
    CUSTOM = 'custom'

class STRUCTURE():
    """ Types of molecular structure
    """
    # Geometry #
    OPT_GEOM_XYZ = 'opt_geom_xyz'
    OPT_GEOM_INT = 'opt_geom_internal'
    INIT_GEOM_XYZ = 'init_geom_xyz'
    INIT_GEOM_INT = 'init_geom_internal'
    # Rotational Constants #
    EQUIL_ROT_CONST = 'equil_rot_constant'

class BASIS():
    """ Various Basis Sets
    """
    # Dunning Correlation-Consistent Basis Sets #
    PVDZ = 'cc-pvdz'
    PVTZ = 'cc-pvtz'
    PVQZ = 'cc-pvqz'

class PROGRAM():
    """ Programs to be called
    """
    # Electronic Structure Programs #
    CFOUR = 'cfour2'
    GAUSSIAN = 'gaussian09'
    MOLPRO = 'molpro2015'
    MOLPRO_MPPX = 'molpro2015-mppx'
    MRCC = 'mrcc2018'
    NWCHEM = 'nwchem6'
    ORCA = 'orca4'
    PSI4 = 'psi4'
    QCHEM = 'qchem'
    # Kinetics Programs #
    MESS = 'mess'
    # Other Programs #
    ESTOKTP = 'estoktp'
