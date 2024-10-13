import os 
os.system("cls")
def descomponer(cantidad):
    billetes = [200, 100, 50, 20, 10, 5, 2, 1]
    return {valor: cantidad // valor for valor in billetes}

cantidad = float(input("cantidad: s/,"))
resultado = descomponer(cantidad)
for valor, cant in resultado.items():
    print(f"S/.) {valor}: {cant}")