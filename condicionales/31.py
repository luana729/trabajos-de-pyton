import os 
os.system("cls")

def sueldo(cat, h):
    tarifas = {'A': 21, 'B': 19.5, 'C': 17, 'D': 15.5}
    sb = h * tarifas[cat]
    desc = sb * (0.2 if sb > 2500 else 0.15)
    return {'Bruto': sb, 'Descuento': desc, 'Neto': sb - desc}

cat = input("Categoría (A-D): ").upper()
h = float(input("Horas: "))
print(sueldo(cat, h))