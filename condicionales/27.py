import os 
os.system("cls")

def calcular_sueldo(ventas):
    sb = 600 + ventas * 0.15
    desc = sb * (0.1 if sb > 1800 else 0.05)
    polos = 3 if ventas > 1000 else 1
    return sb, desc, sb - desc, polos

ventas = float(input("Ventas: "))
sb, desc, sn, polos = calcular_sueldo(ventas)
print(f"Sueldo bruto: S/. {sb:.2f}\nDescuento: S/. {desc:.2f}\nSueldo neto: S/. {sn:.2f}\nPolos: {polos}")