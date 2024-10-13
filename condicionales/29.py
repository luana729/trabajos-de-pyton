import os 
os.system("cls")

def sueldo(h, t):
    hb = 48 * t
    he = max(0, h - 48) * t * 1.2
    sb = hb + he
    desc = sb * 0.11 if sb > 1500 else 0
    return {'Horas': h, 'Tarifa': t, 'Bruto': sb, 'Descuento': desc, 'Neto': sb - desc}

horas = float(input("Horas: "))
tarifa = float(input("Tarifa (S/): "))
print(sueldo(horas, tarifa))