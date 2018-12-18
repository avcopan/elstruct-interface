
def write_lccsdt(geom, mult, basis='reg'):
  ''' writes a file to do lccsdt calculations for a series of basis sets in Molpro '''  

  # Determine which ccsd method to use
  if mult == '1':
    method = 'df-lccsd(t)'
  else:
    method = 'df-luccsd(t)'

  # Determine which basis set series to use
  if basis == 'reg':
    basis_sets = ['cc-pVDZ', 'cc-pVTZ', 'cc-pVQZ', 'cc-pV5Z']
  elif basis == 'aug':
    basis_sets = ['aug-cc-pVDZ', 'aug-cc-pVTZ', 'aug-cc-pVQZ', 'aug-cc-pV5Z']

  # Head of file string
  head_str = '''memory,1000,m
gthresh,energy=1.0d-10,orbital=1.0d-10

nosym
angstrom
Geometry = {\n'''
  
  # String with close to the geometry section
  geom_close_str = '''}}\n
set,charge=0
set,spin={0}
\n'''.format( str(int(mult)-1) ) 

  # String containing the theoretical method
  method_str = ''
  for i in range(len(basis_sets)):
    method_str = method_str + '''basis={0}
{{df-rhf,maxit=300}}
{{{1},maxit=150}}
e{2} = energy
\n'''.format( basis_sets[i], method, basis_sets[i].split('V')[1] ) 
  
  # Energy print string
  energy_print_str = '''show,eDZ
show,eTZ
show,eQZ
show,e5Z
\n'''

  # Write the head of the input file
  with open('input.dat','w') as infile:
    
    infile.write(head_str)
    
    for i in range(len(geom)):
      infile.writelines(geom[i])
    
    infile.write(geom_close_str)
    infile.write(method_str)
    infile.write(energy_print_str)

  return None


