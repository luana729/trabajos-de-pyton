import os 
os.system("cls")

def mayor_numero(num):
  digitos = sorted(str(num))
  return int(digitos[-1] + digitos[0])

numero = int(input("Ingrese un número de 4 cifras: "))
print("El mayor número de dos cifras es:", mayor_numero(numero))