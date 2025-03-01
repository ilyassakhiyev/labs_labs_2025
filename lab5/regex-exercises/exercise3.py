import re

text = 'shdhiwi_jd_ij_di_dksdkals_smam'

x = re.findall('[a-z]+_', text)

print(x)