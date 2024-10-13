import os 
os.system("cls")

def sueldo(ventas):
    basico = 500
    comision = ventas * 0.09
    bruto = basico + comision
    neto = bruto * 0.89
    return comision, bruto, bruto - neto, neto

ventas = float(input("ventas: s/."))
c, b, d, n = sueldo(ventas)
print(f"comision: S/. {c: .2f}, Bruto: s/. {b: .2f}, Descuento: s/. {d: .2f}, Neto: s/. {n:.2f}")