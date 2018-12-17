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
    captures = ref.captures(pattern, output)

    if not captures:
        raise ValueError("No energy found in ouput!")

    energy = float(captures[-1])
    return energy

