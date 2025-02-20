from math import *

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))

a = l / (2 * tan(radians(180 / n)))

A = (n * l * a) / 2

print("The area of the polygon is:", A)