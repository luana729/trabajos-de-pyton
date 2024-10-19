# programas un algoritmo recursivo que permita invertir un numero. 
# Ejemplo Entrada:123 Salida:321
import os
os.system("cls")

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

def pedir_numero():
    entrada = input("Introduce un número entero positivo (o 'salir' para terminar): ")
    if entrada.lower() == 'salir':
        return
    try:
        numero = int(entrada)
        if numero < 0:
            print("Por favor, introduce un número entero positivo.")
        else:
            resultado = suma_digitos(numero)
            print(f"La suma de los dígitos de {numero} es: {resultado}")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
    
    # Llamada recursiva para pedir otro número
    pedir_numero()

# Llamar a la función inicial
pedir_numero()
