import  os
os.system

def es_par(n):
    # caso base: si n es 0, es par
    if n == 0:
        return True 
    else: 
     return es_impar(n -1)
    
def es_impar(n):
   # caso base: si n es 0, no es impar
   if n == 0:
      return False
   else:
      return es_par(n -1)
   
# ejemplo de uso
numero = 10 # cambia este valor para probar con otros numeros
if  es_impar(numero):
   print(f"{numero} es impar.")
else:
   print(f"{numero} es par.")
