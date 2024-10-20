import statistics

def calcular_estadisticas(lista):
  """Calcula el menor, mayor y promedio de una lista de números.

  Args:
    lista: Una lista de números.

  Returns:
    Una tupla con el menor, mayor y promedio.
  """

  menor = min(lista)
  mayor = max(lista)
  promedio = statistics.mean(lista)
  return menor, mayor, promedio

# Pedimos al usuario que ingrese los números
numeros = [int(num) for num in input("Ingrese 10 números separados por espacios: ").split()]

# Verificamos si el usuario ingresó exactamente 10 números
if len(numeros) != 10:
  print("Debe ingresar exactamente 10 números.")
else:
  # Calculamos las estadísticas y las mostramos
  menor, mayor, promedio = calcular_estadisticas(numeros)
  print(f"El número menor es: {menor}")
  print(f"El número mayor es: {mayor}")
  print(f"El promedio es: {promedio}")