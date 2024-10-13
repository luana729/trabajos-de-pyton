import os 
os.system("cls")

def edades_extremos(edades):
    return min(edades), max(edades)

edades = [int(input("Edad {}: " . format(i+1))) for i in range(3)] 
menor , mayor = edades_extremos(edades)
print(f"la edad menor es: {menor}")
print(f"la edad mayor es: {mayor}")