import os 
os.system("cls")

import math

def calcular_hipotenusa(cateto1, cateto2):
  """Calcula la hipotenusa de un triángulo rectángulo.

  Args:
    cateto1: La longitud de un cateto.
    cateto2: La longitud del otro cateto.

  Returns:
    La longitud de la hipotenusa.
  """

  hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
  return hipotenusa

# Pedimos al usuario que ingrese los catetos
cateto1 = float(input("Ingrese la longitud del primer cateto: "))
cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

# Calculamos la hipotenusa
resultado = calcular_hipotenusa(cateto1, cateto2)

# Mostramos el resultado
print("La hipotenusa es:", resultado)