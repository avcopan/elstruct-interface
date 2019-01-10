""" 
Script parses the output files from Molpro 2015 
to obtain information of interest.

Retrieves: 
1. Energy (initial, final from opt, energy at each opt step)
2. Geometry (initia, final from opt, geom at each opt step)
3. Gradient (internal, xyz)
4. Hessian (internal, xyz)
5. ZPVE
6. Dipole Moment
"""

__updated__ = "2019-01-10"
__authors__ = "Muray Keceli, Sarah Elliott, Kevin Moore, Andreas Copan"


from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params


#### Library of String Patterns to locate pieces of information in file #####

# Dictionary for strings to find the energies in the files
# Supported: RHF, UHF, MP2, CCSD, [R/U/]CCSD(T), CASSCF (MULTI?), RS2, RS2C, MRCISD_Q, CUSTOM
ENERGY_PATTERNS = {
    params.METHOD.RHF: (
        '!RHF STATE' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.one_or_more(relib.FLOAT) + 
        rep.one_or_more(relib.WHITESPACE) +
        'Energy' + 
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    ),
    params.METHOD.UHF: (
        '!UHF STATE' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.one_or_more(relib.FLOAT) + 
        rep.one_or_more(relib.WHITESPACE) +
        'Energy' + 
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    ),
    params.METHOD.MP2: ( 
        'MP2 total energy:' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.capturing(relib.FLOAT)
    )
    params.METHOD.RMP2: ( 
        '!RHF-RMP2 energy' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.capturing(relib.FLOAT)
    )
    params.METHOD.UMP2: ( 
        '!RHF-UMP2 energy' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.capturing(relib.FLOAT)
    )
    params.METHOD.CCSD: (
        '!CCSD total energy' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.capturing(relib.FLOAT)
    )
    params.METHOD.CCSD(T): (
        '!CCSD(T) total energy' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.capturing(relib.FLOAT)
    )
    params.METHOD.RCCSD(T): ( 
        '!RHF-RCCSD(T) energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )    
    params.METHOD.UCCSD(T): (
        '!RHF-UCCSD(T) energy' +
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )
    params.METHOD.CASSCF: ( 
        '!MCSCF STATE' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.one_or_more(relib.FLOAT) + 
        rep.one_or_more(relib.WHITESPACE) +
        'Energy' + 
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )
    params.METHOD.CASPT2: ( 
        '!RSPT2 STATE' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.one_or_more(relib.FLOAT) + 
        rep.one_or_more(relib.WHITESPACE) +
        'Energy' + 
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )
    params.METHOD.icCASPT2: (
        '!RSPT2 STATE' + 
        rep.one_or_more(relib.WHITESPACE) + 
        rep.one_or_more(relib.FLOAT) + 
        rep.one_or_more(relib.WHITESPACE) +
        'Energy' + 
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT)
    )
    params.METHOD.MRCISD_Q: (
        'Cluster corrected energies' +                
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) +
        rep.one_or_more(relib.WHITESPACE) +
        '(Davidson, fixed reference)'
    )
    params.METHOD.CUSTOM: ( 
        'SETTING E_' + 
        rep.capturing(STRING) + 
        '=' + 
        rep.one_or_more(relib.WHITESPACE) +
        rep.capturing(relib.FLOAT) 
}

# Patterns for searching for Structural information
INIT_GEOM_PATTERN = 'ATOMIC COORDINATES' 
GEOM_OPT_STEP_PATTERN = 'Current geometry (xyz format, in Angstrom)' 

ROT_CONSTANT_PATTERN = (
    'Rotational constants:' +
    rep.one_or_more(relib.WHITESPACE) +
    rep.capturing(relib.FLOAT) +
    rep.one_or_more(relib.WHITESPACE) +
    rep.capturing(relib.FLOAT) +
    rep.one_or_more(relib.WHITESPACE) +
    rep.capturing(relib.FLOAT) +
    rep.one_or_more(relib.WHITESPACE) +
    'GHz  (calculated with average atomic masses)'
)

# Patterns for searching for vibrational frequency information
HESS_START_LINE = 'Force Constants (Second Derivatives of the Energy)'
HESS_END_LINE = 'Atomic Masses'

VIB_FREQ_PATTERN = 'Wavenumbers \[cm-1\]   (.+)'

ZPVE_PATTERN = (
    'Zero point energy:' +
    rep.one_or_more(relib.WHITESPACE) +
    rep.capturing(relib.FLOAT) +
    rep.one_or_more(relib.WHITESPACE) +
    '[H]' +
    rep.one_or_more(relib.WHITESPACE) +
    rep.capturing(relib.FLOAT) +
    rep.one_or_more(relib.WHITESPACE) +
    '[1/CM]' +
    rep.one_or_more(relib.WHITESPACE) +
    rep.capturing(relib.FLOAT) +
    rep.one_or_more(relib.WHITESPACE) +
    '[KJ/MOL]'
)

# Patterns for other molecular properties
DIPOLE_MOM_PATTERN = 'Permanent Dipole Moment \[debye\]'

# Patterns for other utilities (note that job could finish with Error messages) 
JOB_FINISH_PATTERN = 'Variable memory released'                         # Line printed if Molpro exits normally 
E_ITER_FAIL_PATTERN = ''                                                # Printed when SCF, CC, iterations fail to converge 
GEOM_OPT_FAIL_PATTERN = 'No convergence in max. number of iterations'   # Printed when geom. opt fails to converge 



##### Functions for determining helpful information from file ####

def calc_natom()
  ''' Determines the number of atoms of the molecule in the file 
  '''
  return natom

def det_mol_type()
  ''' Determines if the molecule in the file is an atom, linear molecule, or nonlinear molecule
  '''
  return

def determine_job_type(lines):
  ''' Determines what type of calculations were performed in the job
  '''
    
    job_type = 'single point energy'

    if 'optg' in lines:
       job_type += 'geometry optimization'
    elif 'freq' in lines:
       job_type += 'harmonic frequency'

  return job_type


#### Functions for Grabbing Information #####

### Grab Structural Information ###

def geometry(lines, coords='xyz', choice='final')
  ''' Finds all the geometries in a file 
      Returns geometry in xyz or internal coordinates, in Angstrom
  '''

  # Get the number of atoms
  natom = calc_natom(lines)

  # Get geometries requested by user
  if choice == 'initial':
    # Grabs initial xyz (only xyz avail) for debug purpose
    search INIT_GEOM_PATTERN in file for linenum
    for line in lines[ linenum + 4, linenum + 4 + natom + 1 ]    
  
  else:
    # Grabs other geometries 
    search GEOM_OPT_STEP_PATTERN in file for linenums
    for num in linenums

    if choice == 'final':
      geom = geoms[-1]
    if choice == 'all':
      geom = geoms

  return geom

# from patools
def zmat(lines):
    geolines =  lines.split('geometry={')[1].split('}')[0].split('\n')[1:-1]
    zmat = 'geometry={angstrom \n' + '\n'.join(geolines) + '\n}\n'
    optzmat = False
    if 'OPTG' in lines:
        optzmat = True
        lines = lines.split('END OF GEOMETRY OPTIMIZATION')[0].split('Variable')[-1].split('\n')
        lines = lines[3:-3]
        for line in lines:
            zmat += line.split()[0].lower() + ' =  ' + line.split()[4] + '\n'
    if optzmat:
        return zmat
    return None

# from patools
def geo(lines):
    lines =  lines.split('Current geometry (xyz format')
    if len(lines) > 1:
        lines = lines[-1].split('************')[0]
        lines =  lines.split('\n')[4:]
        return '\n'.join(lines)
    else:
        lines =  lines[0].split('Dump information in style XYZ')
        if len(lines) > 1:
            lines = lines[-1].split('************')[0]
            lines =  lines.split('\n')[4:]
            return '\n'.join(lines)
    return

def equil_rot_consts(lines):
  ''' Reads the equilibrium rotational constants corresponding to the FINAL GEOMETRY in the output file.
      Returns the rotational constants as a list of strings; in cm-1. 
  '''

    # Locate all rotation constants, grab the last one.
    all_equil_rot_constants = re.findall(ROT_CONSTANT_PATTERN,lines)
    equil_rot_constants = all_equil_rot_constants[-1].split()[1:4]
   
    # Convert to cm-1 
    for constant in equil_rot_constants:
      constant *= GHz_to_cm

    return equil_rot_constants

### Grab Vibrational Frequency Stuff ###

def vib_freqs(lines):
  ''' Reads the harmonic vibrational frequencies from the output file.
      Returns the frequencies as a list in cm-1.
  '''

    freqs_str = 'Wavenumbers \[cm-1\]   (.+)'
    freqlines = re.findall(freqs_str, lines)
    freqs = []
    for line in freqlines:
        if line.split()[0].strip() != '0.00': 
            freqs.extend(line.split())
    
    return freqs

# partially from patools
def hessian(lines, symmetry=False):
  ''' Reads the unprojected Cartesian Hessian from the output file.
      Returns the Hessian in a string; in UNITS
      TODO: (1) Grabber only works if job is run without symmetry
            (2) Convert Hessian to a full Hessian? or lower/upper Triangular?
  '''

    # Isolate block of lines from output file containing the Hessian    
    start_line_num = io.get_line_number( HESS_START_LINE, lines=lines ) + 1
    end_line_num   = io.get_line_number( HESS_END_LINE, lines=lines ) - 2
    hess_lines = lines.split()[ start_line_num, end_line_num ] 
    if start_line < 0:
        return ''
    hess = ''

    # Read the Hessian 
    if symmetry == False:

      for line in lines[sline+1:eline-2]:
        hessline = ''
        for val in line.split():
          if 'G'  in val:
            if 'GX' in val:
              add = 1
              val = val.replace('GX','')
            elif 'GY' in val:
              add = 2
              val = val.replace('GY','')
            else:
              add = 3
              val = val.replace('GZ','')
            val =  str( (int(val) - 1 ) * 3 + add)
        hessline += '\t' +  val
      hess +=  hessline + '\n'
    
    else:

      Code     


    return hess


def zpve(lines):
  ''' Reads the zero-point vibrational energy (ZPVE) from the output file.
      Returns the ZPVE as a string; in Hartrees. 
  '''
  
    zpve = re.findall(ZPVE_PATTERN, lines)
    if len(zpve) > 0:
        return float(zpve[-1])
    return zpve


### Grab Energies ###

def single_point_energy(lines, theory, choice='final' )
  ''' Obtains a single or series of single point energies  
      Returns energy in Hartrees.
  '''

    assert theory in ENERGY_PATTERNS.keys()
    energy_pattern = ENERGY_PATTERNS[theory]
    
    # Find the energy in the file
    energies = re.find
    if capture is None:
        raise ValueError("No energy found in ouput!")

    if choice == 'initial':
      energy = energies[0]
    elif choice == 'final':
      energy = energies[-1]
    elif choice == 'all':
      energy = energies

  return energy
 
def optimization_energy()
  ''' Grabs energy along the optimization path 
      Returns energy in Hartrees.
  '''

  return

def relaxed_scan_energy()

  return

### Grab Molecular Properties ###

def dipole_moment(lines):
  ''' Reads the Permanent Dipole moment from the output file.
      Returns the constants as a list of strings; in Debye. 
  '''

    # Locate the last instance of the dipole moment
    lines = lines.splitlines()
    dipole_str = 'Permanent Dipole Moment \[debye\]'
    dipole_line = io.get_line_number(dipole_str,lines=lines) + 1
    
    # Read the dipole moment
    if len(dipole_line) > 1:
      dipole_moment = dipole_line.strip.split()[2:] 
    else:
      dipole_moment = []
      print('No Dipole Moment Found in File')

  return dipole_moment


##### Other useful functions #####

def assess_job_status(lines)
  ''' Checks if the job completes successfully.
      Returns job status and any error messages located
      PSEUDOCODE BELOW
  '''

   search JOB_FINISH_PATTERN in file
   search OTHER_ERROR_PATTERNS in file
  
  if JOB_FINISH_PATTERN in file
    job_complete = True

  if OTHER_ERROR_PATTERNS in file
    error_msg = message
  else:
    error_msg = ''

  if job_complete == True and error_msg == '':
    job_status = 'Success'
  else:
    job_status = 'Failure'

  return job_status, error_msg

