import re

text = "aaaabbbbbbbbbb"
x = re.fullmatch('a*b*', text)

if x:
    print(x.group())
else:
    print("No match")