memory,500,m
gthresh,orbital=1.d-${thresh_log}

angstrom
Geometry = {
${geom}
}

basis=${basis}

{rhf,maxit=${niter}
 wf,${nelec},${irrep},${spin},${charge}}

