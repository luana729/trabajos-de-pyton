import os
os.system("cls")

def longitud_cadena(cadena):
    #caso base: si la cadena esta vacia, la longitud es 0 
    if cadena == "":
        return 0
    else:
        # contar el primer caracter y llamar recursivamente con el de la cadena 
        return 1 + longitud_cadena(cadena[1:])
    
# ejemplo de uso 
resultado = longitud_cadena("hola")
print(f"la longitud de 'hola'es {resultado}") # salida: 4

resultado = longitud_cadena("recursividad")
print(f" la longitu de 'recursividad'es:{resultado} ") # salida: 12
