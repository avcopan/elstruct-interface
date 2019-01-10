${comment}
${geom}

*CFOUR(CALC_LEVEL=HF
REFERENCE=RHF,BASIS=${basis}
SCF_CONV=${thresh_log}
MEMORY_SIZE=${memory},MEM_UNIT=GB
CHARGE=${charge},MULTIPLICITY=${mult})


