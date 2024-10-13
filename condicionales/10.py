import os 
os.system("cls")

def promedio_sin_extremos(notas):
    notas.sort()
    return sum(notas[1:-1]) / len(notas[1:-1])

notas = [float(input(f"notas {i+1}: ")) for i in range(5)]
print("promedio (sin extemos):" , promedio_sin_extremos(notas))
