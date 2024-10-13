import os 
os.system("cls")

def promedio_final(n1, n2, n3):
  return (n1 + n2 + max(n3, 10) + 2) / 3

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
print("Promedio:", promedio_final(nota1, nota2, nota3))