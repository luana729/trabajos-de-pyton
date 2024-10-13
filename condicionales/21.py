import os 
os.system("cls")

def info_empleado(num):
    return {1: "soltero", 2: "casado", 3: "divorciado", 4: "viudo"}[num // 1000], (num % 1000) // 10, {1: "masculino", 2: "femenino"}[num % 10]

num = int(input("Número de empleado: "))
estado, edad, sexo = info_empleado(num)
print(f"Estado civil: {estado}\nEdad: {edad}\nSexo: {sexo}")