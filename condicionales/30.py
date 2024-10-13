import os 
os.system("cls")

def cuota(c, d):
    return c - max(5, c*0.02) if d <= 10 else c + max(10, c*0.03) if d <= 20 else c

cuota = float(input("Cuota: "))
dia = int(input("Día de pago: "))
print(f"A pagar: S/. {cuota(cuota, dia)}")