import os 
os.system("cls")

import math

r = float(input("Ingrese el radio del cilindro: "))
h = float(input("Ingrese la altura del cilindro: "))

area_base = math.pi * r**2
area_lateral = 2 * math.pi * r* h
area_total = 2 * area_base + area_lateral

print(f"Area base : {area_base: .2f}")
print(f"Area lateral: {area_lateral: .2f}")
print(f"Area total: {area_total:.2f}")
