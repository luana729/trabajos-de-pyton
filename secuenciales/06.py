import os 
os.system("cls")

import math

def calcular_cilindro(radio, altura):
  """Calcula el área total y el volumen de un cilindro.

  Args:
    radio: El radio del cilindro.
    altura: La altura del cilindro.

  Returns:
    Una tupla con el área total y el volumen del cilindro.
  """

  area = 2 * math.pi * radio * (radio + altura)
  volumen = math.pi * radio**2 * altura

  return area, volumen

# Solicitar al usuario el radio y la altura
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Calcular el área y el volumen
area_total, volumen = calcular_cilindro(radio, altura)

# Mostrar los resultados
print(f"El área total del cilindro es: {area_total:.2f} unidades cuadradas")
print(f"El volumen del cilindro es: {volumen:.2f} unidades cúbicas")
