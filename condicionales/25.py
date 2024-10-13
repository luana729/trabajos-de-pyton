import os 
os.system("cls")

def bonificacion(sueldo, hijos):
    return sueldo * (0.125 if hijos > 1 else 0.1) + hijos * 40 if hijos > 1 else 0

sueldo = float(input("Sueldo: "))
hijos = int(input("Hijos: "))
print(f"Bonificación: S/. {bonificacion(sueldo, hijos)}")