import os 
os.system("cls")

# leer un numero entero de 4 cifras
numero = input("ingrese un numero entero de 4 cifras: ")

#Asegurate de que el numero tiene 4 cifras 
if len(numero) ==4 and numero.isdigit():
    suma_cifras = sum(int(digito)  for digito in numero)
    print(f"la suma de las cifras es: {suma_cifras}")
else: 
    print("por favor , ingrese un numero valido de 4 cifras. ")
