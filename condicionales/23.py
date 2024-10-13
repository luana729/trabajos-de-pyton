import os 
os.system("cls")

def propina(m, f):
  return m + (3 if m > 17 else m) + f + (2 if f > 15 else 0.5), "¡Ganaste un reloj!" if (m+f)/2 > 16 else ""

m, f = float(input("Mat: ")), float(input("Fís: "))
print(f"Propina: S/. {propina(m, f)[0]}\n{propina(m, f)[1]}")