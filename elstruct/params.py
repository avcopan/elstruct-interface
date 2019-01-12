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
    OPT = 'opt'

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

class FREQUENCY():
    """ Frequency Information
    """    
    HARM_FREQ = 'harm_freq'
    ANHARM_FREQ = 'anharm_freq'
    HARM_ZPVE = 'harm_zpve'
    ANHARM_ZPVE = 'anharm_zpve'
    ANHARM_MATRIX = 'anharm_matrix'
    CENTRIG_DIST_CONST = 'centrig_dist_const'
    VIBROT_MATRIX = 'vibrot_matrix'
    
class SURFACE():
    """ Information about the Potential Energy Surface
    """
    GRADIENT_XYZ = 'grad_xyz'
    GRADIENT_INT = 'grad_internal'
    HESSIAN_XYZ = 'hessian_xyz'
    HESSIAN_INT = 'hessian_int'

class PROPERTY():
    """ Molecular Properties of interest
    """
    DIPOLE_MOMENT = 'dipole_moment'

class STATUS():
    """ Checking on the status of a job
    """
    JOBTYPE = 'jobtype'
    ERROR_CHK = 'error_chk'
    COMPLETE = 'complete'

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
