
def write_dlpno_ccsdt(geom,mult):
  ''' writes a file to do dlpno-ccsd(t) calculations for a series of basis sets in Orca '''  

  # Set the reference via the multiplicity (need to change if ROHF wanted)
  if mult == '1':
    reference = 'RHF'
  else:
    reference = 'UHF'

  # Set the basis sets reset for augmented basis sets
  if basis == 'aug':
    basis_sets = ['aug-cc-pVDZ aug-cc-pVDZ/C', 'aug-cc-pVTZ aug-cc-pVTZ/C', 'aug-cc-pVQZ aug-cc-pVQZ/C', 'aug-cc-pV5Z aug-cc-pV5Z/C']
  else:
    basis_sets = ['cc-pVDZ cc-pVDZ/C', 'cc-pVTZ cc-pVTZ/C', 'cc-pVQZ cc-pVQZ/C', 'cc-pV5Z cc-pV5Z/C']

  # Write the Orca input file
  with open('input.dat','w') as orcafile:
    for j in range(len(basis_sets)): 
      orcafile.write('''#{0}
% pal nprocs 8 end
% MaxCore 12500
! {1} DLPNO-CCSD(T) RIJCOSX GridX5   
! {2} AutoAux
! TightSCF TightPNO
%base"/scratch/kmoore/test{3}" 
* xyz 0 {4}\n'''.format(names[i],reference,basis_sets[j],str(j),mults[i]))
      for k in range(len(structs[i])):
        orcafile.writelines(structs[i][k])
      if j != (len(basis_sets) - 1):
        orcafile.write('*\n$new_job\n')
      else:
        orcafile.write('*\n')

  return None    
