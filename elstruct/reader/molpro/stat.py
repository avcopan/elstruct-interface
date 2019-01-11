""" Check job status
"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-11"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params


# Patterns for other utilities (note that job could finish with Error messages) 
JOB_FINISH_PATTERN = 'Variable memory released'                         # Line printed if Molpro exits normally 
E_ITER_FAIL_PATTERN = ''                                                # Printed when SCF, CC, iterations fail to converge 
GEOM_OPT_FAIL_PATTERN = 'No convergence in max. number of iterations'   # Printed when geom. opt fails to converge 


def determine_job_type(lines):
    """ Determines what type of calculations were performed in the job
    """
    
    job_type = 'single point energy'

    if 'optg' in lines:
        job_type += 'geometry optimization'
    elif 'freq' in lines:
        job_type += 'harmonic frequency'

    return job_type


##### Other useful functions #####

def assess_job_status(lines)
    """ Checks if the job completes successfully.
        Returns job status and any error messages located
        PSEUDOCODE BELOW
    """

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
