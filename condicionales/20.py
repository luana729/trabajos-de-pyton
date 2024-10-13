import os 
os.system("cls")

def orden(a, b, c):
    return "Ascendente" if a <= b <= c else "Descendente" if a >= b >= c else "Desordenado"

a, b, c = map(int, input("Ingrese tres números separados por espacios: ").split())
print(f"El orden es: {orden(a, b, c)}")