import os
os.system

def contador_digitos(n):
    # caso base: si n es 0, mo hay mas digitos 
    if n == 0:
     return 0
    else:
# llamada recursiva para el numero reducido
     return 1 + contador_digitos(n // 10)
    
# ejemplo de uso 
numero = 12345
if numero ==0:
  resultado = 1 # para manejar el caso de que el numero sea 0
else:
    resultado = contador_digitos(numero)
print(f"el numero {numero} tiene  {resultado}  digitos.")


