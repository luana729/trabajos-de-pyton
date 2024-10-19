import os
os.system("cls")

def potencia(base, exponente):
 # caso base: cualquier numero elevado a 0 es 1
 if exponente == 0:
    return 1
 else:
    # calcular la potencia recursivamente
    return base * potencia(base,  exponente- 1)
# ejemplo de uso 
resultado = potencia(2,3)
print(f"2 elevado a 3 es: {resultado}") #salida: 8

resultado = potencia(5, 0)
print(f"5 elevado a 0 es: {resultado}") # salida:1
