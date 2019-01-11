""" Other useful?
"""

#def get_line_number(keyword, lines=None, filename=None, getlastone=False):
#    """
#    Returns the line number of a keyword found in given lines of string.
#    Returns -1 if keyword is not found
#    """
#    num = -1
#    if lines is None and filename is None:
#        logging.debug('List of lines or a filename to be read is required for get_line_number')
#    elif filename:
#        lines = read_file(filename, aslines=True)
#
#    for n, line in enumerate(lines):
#        if keyword in line:
#            if getlastone:
#                num = n
#            else:
#                return n
#    return num
