""" output file readers for molpro
"""
from ..rere import find as ref
from ..rere import pattern as rep
from ..rere import pattern_lib as relib
from ... import params

#PATTERNS = {
#    params.METHOD.RHF: (
#        'Final Energy:' + rep.one_or_more(relib.WHITESPACE) +
#        rep.capturing(relib.FLOAT)
#    ),
#    params.METHOD.CCSD: (
#        'CCSD total energy' + rep.one_or_more(relib.WHITESPACE) + '=' +
#        rep.one_or_more(relib.WHITESPACE) + rep.capturing(relib.FLOAT)
#    )
#}


def energy(theory, output):
    assert theory in PATTERNS.keys()
    pattern = PATTERNS[theory]
    capture = ref.last_capture(pattern, output)

    if capture is None:
        raise ValueError("No energy found in ouput!")

    return float(capture)
