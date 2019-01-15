def gaussian_islinear(s):
    """
    Returns true if the molecule is linear for the given log.
    """
    if "Linear Molecule" in s or gaussian_natom(s) == 2:
        return True
    else:
        return False
    
def gaussian_natom(s):
    """
    NAtoms=     30 NQM=       30 NQMF=       0 NMMI=      0 NMMIF=      0
    """
    from . import iotools as io
    if type(s) == str:
        lines = s.splitlines()
    keyword = 'NAtoms='
    n = io.get_line_number(keyword, lines=lines)
    return int(lines[n].split()[1])

def gaussian_nfreq(s):
    """
    Return the number of vibrational degrees of freedom for
    a given log.
    """
    natom = gaussian_natom(s)
    if gaussian_islinear(s):
        nvdof = 3*natom - 5
    else:
        nvdof = 3*natom - 6
    return nvdof

  
def gaussian_basisset(lines):

    bas = 'Standard basis:\s*(\S*)'
    bas = re.findall(bas,lines)
    bas[-1] = bas[-1].replace('(d)','*')
    return bas[-1]

def gaussian_method(lines):

    method = 'Done:\s*E\((\w+)'
    method = re.findall(method,lines)
    #if method[-1].strip().upper() == 'CORR' or method[-1].strip().upper() == 'Z':
    if 'CCSD(T)' in lines:
        return 'CCSD(T)'
    elif 'CCSD' in lines:
        return 'CCSD'
    method = method[-1].lstrip('r').lstrip('u').lstrip('R').lstrip('U')
    if 'HF' in method:
        if 'MP2' in lines:
            return 'MP2'
        if 'MP4' in lines:
            return 'MP4'
    return method

def gaussian_energy(lines,method=''):

    if method == '':
        method = gaussian_method(lines)
    if 'CCSD' in method or 'MP' in method:
        method = method.replace('(','\(').replace(')','\)')
    #    energ  = method + '=([u,U,r,R]*[\w,\.,\s,-,D,\+]*)'
        energ  = method + '=([u,U,r,R]*[\w,\.,\s,-]*)'
        energ  = re.findall(energ,lines.replace('\n','').replace(' ',''))
    #    return (method,float(energ[-1].replace('D','E').replace('\n','').replace(' ','')))
        return (method,float(energ[-1].replace('\n','').replace(' ','')))
    else:
        lines = lines.strip().replace('\n','').replace(' ','')
        if 'anharm' in lines:
            energ = 'MP2=\s*([\d,\-,\.,D,\+]*)'
            energ = re.findall(energ,lines)
            if energ:
                return (method, float(energ[-1].replace('D','E')))
            else:
                energ = 'HF=\s*([\d,\-,\.,D,\+]*)'
                energ = re.findall(energ,lines)
                return (method, float(energ[-1].replace('D','E')))
       # energ = '(\S+)\s*A\.U\.'
        energ = 'E\([u,U,r,R]*' + method + '\)\s*=\s*([\d,\-,\.,D,\+]*)'
        energ = re.findall(energ,lines)
        return (method, float(energ[-1].replace('D','E')))
    return 

def gaussian_opt_zmat_params(lines):
    
    params = ''
    if not 'Optimized Parameters' in lines:
        return None
    varis  = lines.split('Optimized Parameters')[1].split('---------------------------------------')
    if 'Definition' in varis[0]:
        varis = varis[2].split('\n')
        for var in varis[1:-1]:
            var = var.split()
            params += ' '+  var[1] + '\t' + var[3] + '\n'
    else:
        varis = varis[1].split('\n')
        for var in varis[1:-1]:
            var = var.split()
            params += ' '+  var[1] + '\t' + var[2] + '\n'
    return params

def gaussian_zmat(lines):

    lines  = lines.split('Z-matrix:\n')
    zmat   = lines[1].split('       Variables:')[0]
    zmat  += 'Variables:\n'
    zmat   = zmat.replace('Charge = ','')
    zmat   = zmat.replace('Multiplicity =','')
    optzmat = gaussian_opt_zmat_params(lines[1])
    if optzmat == None:
        return None
    return zmat + optzmat

def gaussian_freqs(lines):
    """
    Return harmonic frequencies.
    """
    nfreq = gaussian_nfreq(lines)

    freqs = []
    lines = lines.splitlines()
    key = 'Fundamental Bands (DE w.r.t. Ground State)'
    iline = io.get_line_number(key,lines=lines)
    if iline > 0:
        for i in range(nfreq):
            iline += 1
            line = lines[iline]
            cols = line.split()
            freqs.append(cols[-5])
    else:
        lines = '\n'.join(lines)
        kw = 'Frequencies --  (.+)'
        freqlines = re.findall(kw, lines)
        freqs = []
        k = 0
        if len(freqlines) > 0:
            freqs = ['']*nfreq
            for i in range(len(freqlines)):
                tokens = freqlines[i].split()
                for j in range(len(tokens)):
                    freqs[k] = tokens[j]
                    k += 1
                if k == nfreq:
                    break
    return freqs

def gaussian_hessian(lines):
    startkey = 'Force constants in Cartesian coordinates:'
    endkey   = 'Force constants in internal coordinates:'
    key2 = 'Leave Link'
    lines= lines.split('Harmonic vibro-rotational analysis')[-1]
    lines = lines.splitlines()
    sline = io.get_line_number(startkey,lines=lines)
    eline = io.get_line_number(endkey,lines=lines)
    if sline < 0:
        return ''
    hess   = '\n'.join(lines[sline+1:eline]).replace('D','E')
    hess   = hess.split(key2)[0]
    return hess

def gaussian_xyz_foresk(lines):
    atom = lines.split('Distance matrix')[-1].split('Symm')[0]
    if len(atom.split('\n')) > 8:
        atom = atom.split(' 6 ')[0] + ' 6 ' + atom.split(' 6 ')[1]
        atom = atom.split('\n')[2:-2]
    length = len(atom)
    atoms  = []
    for at in atom:
        atoms.extend(at.split()[1])
    xyz = 'Geometry ' + str(length) + ' Angstrom\n'
    if 'Eckart' in lines:
        lines = lines.split('Gaussian Orientation')[-1].split('Eckart')[0]
        lines = lines.split('\n')[5:-2]
        for i,line in enumerate(lines):
            line = line.split()
            xyz += atoms[i] + '  ' + line[2] + '  ' + line[3] + '  ' + line[4] + '\n'
    else:
        lines = lines.split('Coordinates (Angstroms)')[-1].split(' Distance matrix')[0]
        lines = lines.split('\n')[3:-2]
        for i,line in enumerate(lines):
            line = line.split()
            xyz +=  atoms[i] + '  ' + line[3] + '  ' + line[4] + '  ' + line[5] + '\n'
    return xyz 
    
def gaussian_geo(lines):
    atomnum = {'1':'H','6':'C','7':'N','8':'O'}
    xyz = ''
    try:
        if 'Eckart' in lines:
            lines = lines.split('Gaussian Orientation')[-1].split('Eckart')[0]
            lines = lines.split('\n')[5:-2]
            for i,line in enumerate(lines):
                line = line.split()
                xyz += atomnum[line[1]]+ '  ' + line[2] + '  ' + line[3] + '  ' + line[4] + '\n'
        else:
            lines = lines.split('Coordinates (Angstroms)')[-1].split(' Distance matrix')[0].split(' Rotation')[0].split('Symm')[0]
            lines = lines.split('\n')[3:-2]
            for i,line in enumerate(lines):
                line = line.split()
                xyz += ' ' + atomnum[line[1]] + '  ' + line[3] + '  ' + line[4] + '  ' + line[5] + '\n'
    except:
        logging.error('Cannot parse xyz')
    return xyz
   
def gaussian_xyz(lines):
    geo = gaussian_geo(lines) 
    if geo:
        n   = str(len(geo.splitlines()))
        xyz = n + '\n\n' +  geo
    else:
        xyz = ''
    return xyz

def freq_xyz(lines):
    lines = lines.split('Optimized')[1].split('Z-Matrix orientation')[1].split('Distance matrix')[0]
    geo = gaussian_geo(lines) 
    if geo:
        n   = str(len(geo.splitlines()))
        xyz = n + '\n\n' +  geo
    else:
        xyz = ''
    return xyz


def gaussian_rotconstscent(lines):
    startkey = 'Effective Rotational Constants'
    lines = lines.splitlines()
    sline = io.get_line_number(startkey,lines=lines)
    if sline < 0:
        return ''
    rotlines   =  lines[sline+4:sline+7]
    constants = []
    for line in rotlines:
        constants.append(line.split()[1])
    return constants

def gaussian_rotconsts(lines):
    rot = 'Rotational constants\s*\(GHZ\):\s*([\s,\d,\.,\-]*)'     
    rot = re.findall(rot,lines)
    if len(rot) > 0: 
        rot = rot[-1].split()
    ndof  = gaussian_nfreq(lines)
    if ndof < 2:
        rot = rot[1:]
    if len(rot) > 0:
         if abs(float(rot[0])) < 0.000001:
             rot = rot[1:]
    return rot
 
def gaussian_rotdists (lines):
    startkey = 'Quartic Centrifugal Distortion Constants Tau Prime'
    endkey   = 'Asymmetric Top Reduction'
    lines = lines.splitlines()
    sline = io.get_line_number(startkey,lines=lines)
    if sline < 0:
        return ''
    lines  = lines[sline+3:sline+9]
    distlines = []
    for line in lines:
        splitline = line.split()
        if splitline[0] == 'TauP': 
           distlines.append('\t'.join(splitline[1:3]))
        else:
           break
    constants   = '\n'.join(distlines).replace('D','e')
    return constants

def gaussian_vibrot(lines):
    startkey = 'Vibro-Rot alpha Matrix (in cm^-1)'
    ndof  = gaussian_nfreq(lines)
    lines = lines.splitlines()
    sline = io.get_line_number(startkey,lines=lines)
    if sline < 0:
        return ''
    lines =  lines[sline+3:sline+3+ndof]
    for i in range(len(lines)):
       if ')' in lines[i]:
           lines[i] = lines[i].split(')')[1]
       if ndof < 2:
          lines[i] = '\t'.join(lines[i].split()[:-1])
    mat   = '\n'.join(lines).split('---------------')[0]
    return mat
    
