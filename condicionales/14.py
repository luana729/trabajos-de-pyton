import os 
os.system("cls")

import random

def descuento(numero, monto):
  return monto * (0.85 if numero >= 100 and numero % 2 == 0 else 0.95)

numero = random.randint(1, 999)
monto = float(input("Monto de la compra: "))
final = descuento(numero, monto)
print(f"Número: {numero}, Monto final: ${final:.2f}")