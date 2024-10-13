import os 
os.system("cls")

def pies_a_metros(pies, pulgadas):
 return (pies *12 + pulgadas) * 2.54 / 100

# ejemplo de uso 
estatura_metros = pies_a_metros(5, 10)
print(f"la estatura en metros es: {estatura_metros:.2f} m")
