import os 
os.system("cls")

def invertir_numero(numero):
    return int(str(numero)[::-1])

numero = int(input("Ingrese un numero: "))
print("El numero invertido es:" , invertir_numero(numero))
