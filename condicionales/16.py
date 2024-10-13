import os 
os.system("cls")

def cuotas(ingreso, costo):
    inicial = 0.3 if ingreso >= 1250 else 0.15
    cuota = (costo - costo*inicial) / (75 if ingreso >= 1250 else 120)
    return costo*inicial, cuota

ingreso = float(input("Ingreso: "))
costo = float(input("Costo: "))
ini, mens = cuotas(ingreso, costo)
print(f"Inicial: S/.{ini:.2f}, Mensual: S/.{mens:.2f}")