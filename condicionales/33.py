import os 
os.system("cls")

def bono(mt, o):
    p = (10 - min(mt//15, 3)*2) + (10 - min(o, 5)*2)
    return {18:1000, 16:750, 14:500}[p//2*2] or 250

mt = int(input("Minutos de tardanza: "))
o = int(input("Observaciones: "))
print(f"Bonificación: S/. {bono(mt, o)}")