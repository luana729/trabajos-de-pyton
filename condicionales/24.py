import os 
os.system("cls")

def calcular_sueldo(ventas_totales):
  """
  Calcula el sueldo de un vendedor basado en sus ventas totales.

  Args:
    ventas_totales: Monto total de ventas del vendedor.

  Returns:
    El sueldo total del vendedor.
  """

  sueldo_base = ventas_totales * 0.1
  exceso = max(ventas_totales - 5000, 0) // 500
  bonificacion = exceso * 25
  return sueldo_base + bonificacion

# Solicitar las ventas totales al usuario
ventas = float(input("Ingrese el monto total de ventas: S/. "))

# Calcular el sueldo
sueldo = calcular_sueldo(ventas)

# Mostrar el resultado
print("El sueldo del vendedor es: S/.", sueldo)