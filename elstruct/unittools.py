"""
  Library of physical constants and conversion factors
"""


# Physical Constants
kB = 1.38064852e-23   # Boltzmann Constant in J/K (kg.m2)/(s2.K)
h  = 6.62607015e-34   # Planck's Constant in J.s (kg.m2)/(s)
c  = 2.9972548e8      # Speed of Light in m/s 
Na = 6.0221409e23     # Avogadros number in particles/mol
R  = 1.9872036        # gas constant in kcal/mol

# Unit Conversion Factors
amu_to_kg     = 1.66054e-27 
ang_to_m      = 1.0e-10
cm_to_Hart    = 4.556332E-6
cm_to_Hz      = c * 100.0
cm_to_J       = 100.0 * h * c
ev_to_au      = 0.03674930495
Hart_to_kcal  = 627.509608031
Hart_to_J     = 4.3597e-18
kcal_to_kj    = 4.184                 
kj_to_Hart    = 3.8088E-4          

# Dictionary correlating the atomic symbol with the mass in amu
atom_mass = {
 'H'    :   1.007825035,
 'HE'   :   4.00260324,
 'LI'   :   7.0160030,
 'BE'   :   9.0121822,
 'B'    :  11.0093054,
 'C'    :  12.0000000,
 'N'    :  14.003074002,
 'O'    :  15.99491463,
 'F'    :  18.99840322,
 'NE'   :  19.9924356,
 'NA'   :  22.9897677,
 'MG'   :  23.9850423,
 'AL'   :  26.9815386,
 'SI'   :  27.9769271,
 'P'    :  30.9737620,
 'S'    :  31.97207070,
 'CL'   :  34.968852721,
 'AR'   :  39.9623837,
 'K '   :  38.9637074,
 'CA'   :  39.9625906,
 'SC'   :  44.9559100,
 'TI'   :  47.9479473,
 'V'    :  50.9439617,
 'CR'   :  51.9405098,
 'MN'   :  54.9380471,
 'FE'   :  55.9349393,
 'CO'   :  58.9331976,
 'NI'   :  57.9353462,
 'CU'   :  62.9295989,
 'ZN'   :  63.9291448,
 'GA'   :  68.925580,
 'GE'   :  73.9211774,
 'AS'   :  74.9215942,
 'SE'   :  79.9165196,
 'BR'   :  78.9183361,
 'KR'   :  83.911507,
 'RU'   :  84.911794,
 'SR'   :  87.9056188,
 'Y'    :  88.905849,
 'ZR'   :  89.9047026,
 'NB'   :  92.9063772,
 'MO'   :  97.9054073,
 'TC'   :  97.907215,
 'RU'   : 101.9043485,
 'RH'   : 102.905500,
 'PD'   : 105.903478,
 'AG'   : 106.905092,
 'CD'   : 113.903357,
 'IN'   : 114.903882,
 'SN'   : 119.9021991,
 'SB'   : 120.9038212,
 'TE'   : 129.906229,
 'I'    : 126.904473,
 'XE'   : 131.904144,
 'CS'   : 132.905429,
 'BA'   : 137.905232,
 'LA'   : 138.906347,
 'CE'   : 139.905433,
 'PR'   : 140.907647,
 'ND'   : 141.907719,
 'PM'   : 144.912743,
 'SM'   : 151.919728,
 'EU'   : 152.921225,
 'GD'   : 157.924019,
 'TB'   : 158.925342,
 'DY'   : 163.929171,
 'HO'   : 164.930319,
 'ER'   : 165.930290,
 'TM'   : 168.93421,
 'YB'   : 173.938859,
 'LU'   : 174.940770,
 'HF'   : 179.9465457,
 'TA'   : 180.947462,
 'W'    : 183.950928,
 'RE'   : 186.955744,
 'OS'   : 191.961467,
 'IR'   : 192.962917,
 'PT'   : 194.964766,
 'AU'   : 196.966543,
 'HG'   : 201.970617,
 'TL'   : 204.974401,
 'PB'   : 207.976627,
 'BI'   : 208.980374,
 'PO'   : 208.982404,
 'AT'   : 209.987126,
 'RN'   : 222.017571,
 'D'    :   2.014101779,
 '2H'   :   2.014101779,
 'T'    :   3.01604927,
 '3H'   :   3.01604927,
 '3He'  :   3.01602931,
 '6Li'  :   6.0151214,
 '10B'  :  10.0129369,
 '13C'  :  13.003354826,
 '14C'  :  14.003241982,
 '15N'  :  15.00010897,
 '18O'  :  17.9991603,
 '17O'  :  16.9991312,
 '22Ne' :  21.9913831,
 '21Ne' :  20.9938428,
 '26Mg' :  25.9825937,
 '25Mg' :  24.9858374,
 '29Si' :  28.9764949,
 '30Si' :  29.9737707,
 '34S'  :  33.96786665,
 '33S'  :  32.97145843,
 '36S'  :  35.96708062,
 '37Cl' :  36.96590262,
 '36Ar' :  35.96754552,
 '38Ar' :  37.9627325
}

# Dictionary that relates ther rotation symmetry number, sigma, to the point group symmetry. 
# Note: sigma = E + NCn, where there are N Cn rotations 
rot_sym_num = {
  'C1'    : 1,
  'CS'    : 1,
  'CI'    : 1,
  'C2'    : 2,
  'C3'    : 2,
  'C4'    : 4,
  'C5'    : 5,
  'C6'    : 6,
  'C7'    : 7,
  'C8'    : 8,
  'D2'    : 4,
  'D3'    : 6,
  'D4'    : 8,
  'D5'    : 10,
  'D6'    : 12,
  'D7'    : 14,
  'D8'    : 16,
  'C2V'   : 2,
  'C3V'   : 3,
  'C4V'   : 4,
  'C5V'   : 5,
  'C6V'   : 6,
  'C7V'   : 7,
  'C8V'   : 8,
  'C2H'   : 2,
  'C3H'   : 3,
  'C4H'   : 4,
  'C5H'   : 5,
  'C6H'   : 6,
  'D2H'   : 4,
  'D3H'   : 6,
  'D4H'   : 8,
  'D5H'   : 10,
  'D6H'   : 12,
  'D7H'   : 14,
  'D8H'   : 16,
  'D2D'   :  4,
  'D3D'   :  6,
  'D4D'   :  8,
  'D5D'   : 10,
  'D6D'   : 12,
  'D7D'   : 14,
  'D8D'   : 16,
  'S2'    :  1,
  'S4'    :  2,
  'S6'    :  3,
  'S8'    :  4,
  'S10'   :  5,
  'T'     : 12,
  'TH'    : 12,
  'TD'    : 12,
  'O'     : 24,
  'OH'    : 24,
  'I'     : 60,
  'IH'    : 60,
  'CINFV' : 1,
  'DINFV' : 2
}


