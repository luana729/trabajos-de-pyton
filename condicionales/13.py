import os 
os.system("cls")

numero = int(input("Ingrese un número entero positivo de tres cifras: "))

if 100 <= numero <= 999:
    cifras = sorted([numero // 100, (numero // 10) % 10, numero % 10])
    if cifras == [cifras[0], cifras[0] + 1, cifras[0] + 2] or cifras == [cifras[0] + 2, cifras[0] + 1, cifras[0]]:
        print("Las cifras son consecutivas.")
    else:
        print("Las cifras no son consecutivas.")
else:
    print("El número ingresado no es un entero positivo de tres cifras.")
