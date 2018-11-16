molecule{
${charge} ${mult}
${geom}
units angstrom
}

set basis ${basis}
set d_convergence ${thresh_log}
set maxiter ${niter}
energy('scf')
