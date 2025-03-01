import re

text = "msdfnsjandaasacaabbbsdfsdsd"
x = re.search('abb|abbb', text)

if x:
    print(x.group())
else:
    print("No match found")