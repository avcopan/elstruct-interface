molecule{
${charge} ${mult}
${geom}
units angstrom
}

set basis ${basis}
set d_convergence ${scfthresh}
energy('scf')
