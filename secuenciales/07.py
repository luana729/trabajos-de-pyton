import os 
os.system("cls")

def calcular_rectangulo(base, altura):
  """Calcula el área y el perímetro de un rectángulo.

  Args:
    base: La base del rectángulo (debe ser un número positivo).
    altura: La altura del rectángulo (debe ser un número positivo).

  Returns:
    Una tupla con el área y el perímetro del rectángulo.

  Raises:
    ValueError: Si la base o la altura son números negativos o cero.
  """

  if base <= 0 or altura <= 0:
    raise ValueError("La base y la altura deben ser números positivos.")

  area = base * altura
  perimetro = 2 * (base + altura)

  return area, perimetro

try:
  base = float(input("Ingrese la base del rectángulo: "))
  altura = float(input("Ingrese la altura del rectángulo: "))

  area, perimetro = calcular_rectangulo(base, altura)

  print(f"El área del rectángulo es: {area:.2f} unidades cuadradas")
  print(f"El perímetro del rectángulo es: {perimetro:.2f} unidades")

except ValueError as e:
  print(f"Error: {e}")