import re

text = "hdsbbadhbd_dyg3gs56s5habhbdhjbahab"

x = re.findall('.*a.*b', text)

print(x)