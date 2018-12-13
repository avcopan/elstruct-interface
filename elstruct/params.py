class METHOD():
    RHF = 'rhf'
    CCSD = 'ccsd'
    KEYS = (RHF, CCSD)


class BASIS():
    PVDZ = 'cc-pvdz'
    PVTZ = 'cc-pvtz'
    PVQZ = 'cc-pvqz'


if __name__ == '__main__':
    print(METHOD.RHF)
