import re

text = "AhsjduhduiwhudhuwhdihwidNhiwhn"

x = re.findall('[A-Z][a-z]+', text)

print(x)