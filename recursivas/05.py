import os
os .system("cls")

def invertir_cadena(cadena):
    #caso base: si la cadena esta vacia o tiene un solo caracter
    if cadena == "" or len(cadena) == 1:
        return cadena
    else: 
        # tomar el ultimo caracter y llamar recursivamente con el de la cadena
     return cadena[-1 ] + invertir_cadena(cadena[:-1])
    
# ejemplo de uso 
resultado = invertir_cadena("hola")
print(f"la cadena invertida de 'hola' es: {resultado}") # salida:" aloh"

resultado = invertir_cadena("recursividad")
print(f"la cadena invertida de 'recursividad' es: {resultado}") # salida: "dadiviscrucer"