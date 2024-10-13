import os 
os.system("cls")

def distribuir(monto):
    return (monto*0.3, monto*0.5, monto*0.2) if monto >= 10000 else (monto*0.25, monto*0.6, monto*0.15)

monto = float(input("Monto: "))
salud, comedor, bolsa = distribuir(monto)
print(f"Salud: ${salud:.2f}, Comedor: ${comedor:.2f}, Bolsa: ${bolsa:.2f}")