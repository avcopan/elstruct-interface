""" Write files for storing information to be used by estoktp and stored permanently
"""

__authors__ = "Kevin Moore and Andreas Copan"
__updated__ = "2019-01-11"


STORAGE_WRITERS = {
    params.STORAGE.ENERGY = single_val_writer
    params.STORAGE.GEOMETRY = xyz_val_writer
    params.STORAGE.FREQUENCIES = list_writer
    params.STORAGE.GRADIENT = 3x3_matrix_writer
    params.STORAGE.HESSIAN =  3xn_matrix_writer
}

def write():
    """ Writes the storage file.
    """

    return None


