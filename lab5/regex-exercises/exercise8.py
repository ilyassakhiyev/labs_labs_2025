import re

text = "SdnidamodsmoGsamdasS"

x = re.split('(?=[A-Z])', text)

print(x)