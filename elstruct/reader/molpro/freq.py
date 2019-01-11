""" Vibrational properties
"""

__authors__ = "Kevin Moore, Andreas Copan"
__updated__ = "2019-01-11"

#from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
#from ... import params


# Patterns for searching for vibrational frequency information
VIB_FREQ_PATTERN = 'Wavenumbers [cm-1]   (.+)'

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

def vib_freqs(lines):
    """ Reads the harmonic vibrational frequencies from the output file.
        Returns the frequencies as a list in cm-1.
    """

    freqlines = ['aaaaa']
    #freqlines = re.findall(VIB_FREQ_PATTERN, lines)
    freqs = []
    for line in freqlines:
        if line.split()[0].strip() != '0.00':
            freqs.extend(line.split())

    return freqs

def zpve(lines):
    """ Reads the zero-point vibrational energy (ZPVE) from the output file.
        Returns the ZPVE as a string; in Hartrees.
    """

    zpve = float(re.findall(ZPVE_PATTERN, lines)[-1])

    return zpve
