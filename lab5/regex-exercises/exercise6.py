import re

text = 'uduahwudhuahd idnwaundunaund,ad udwna..undunau'

x = re.sub(r"[ ,.]",";", text)

print(x)