""" 
Library of functions to retrieve frequency information from a Molpro 2015 output file.

"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-14"

from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params

def pattern_parser_1(pattern, output_string):

    return


##### Series of functions to read job status information #####

def pattern_parser_1(pattern, output_string):
    """ Status message found
    """

    status_found = ref.has_match(pattern, output_string)

    return status_found

def complete_msg_reader(output_string):
    """ Checks if the job completes successfully.
        Returns job status and any error messages located
        PSEUDOCODE BELOW
    """

    # Line printed if Molpro exits normally 
    job_finish_pattern = '*** Psi4 exiting successfully. Buy a developer a beer!'          

    job_finish = pattern_parser_1(job_finish_pattern, output_string)
   
    return job_finish

STATUS_READERS = {
    params.JOBSTATUS.COMPLETE_CHK = complete_msg_reader,
}    

def status(output_string):
    """ Returns a status thing.
    """
    
    assert stat in STATUS_READERS.keys()

    job_status = STATUS_READERS[stat](output_string)

    return job_status 
