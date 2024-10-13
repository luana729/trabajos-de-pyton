import os 
os.system("cls")

import math 
def ecuacion2doGrado(a, b, c):
    disc = b**2 - 4*a*c
    if disc >= 0:
      return (-b + math. sqrt(disc)) / (2*a) , (-b - math.sqrt(disc)) / (2*a)
    return " no hay soluciones reales"
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("soluciones:" , ecuacion2doGrado(a,b, c))
