import os 
os.system("cls")

def calcular_distancia(km, pies, millas):
    metros = km*1000 + pies/3.2808 + millas*1609
    yardas = metros / 0.9144
    return metros, yardas

km = float(input("km: "))
pies = float( input( "pies:"))
millas = float(input("millas:"))

m, y = calcular_distancia(km, pies, millas)
print(f"Metros: {m:.2f}")
print(f"Yardas: {y:.2f}")
