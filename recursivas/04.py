import os
os.system
def es_palindromo(cadena):
    # caso base: si la cadena esta cavia o tiene un solo caracter , es un palindromo
    if len(cadena) <= 1:
        return True#comparar el primer y el ultimo caracter
    if cadena[0] != cadena[-1]:
        return False
    # llamar recursivamente con el resto de la cadena 
    return es_palindromo(cadena[1:-1])

# Ejemplo de uso
resultado = es_palindromo("radar")
print(f"'radar' es un palindromo: {resultado}") #salida: true

resultado = es_palindromo("hola")
print(f"'hola'es un palindromo: {resultado}") # salida: false