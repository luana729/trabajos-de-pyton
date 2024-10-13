import os 
os.system("cls")

def nombre_dia(numero):
  """Determina el nombre del día de la semana.

  Args:
    numero: Un número entero entre 1 y 7.

  Returns:
    Una cadena con el nombre del día correspondiente.
  """

  dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
  if 1 <= numero <= 7:
    return dias_semana[numero - 1]
  else:
    return "Número inválido. Ingrese un número entre 1 y 7."

# Pedir al usuario que ingrese un número
numero_dia = int(input("Ingrese un número del 1 al 7 para el día de la semana: "))

# Obtener y mostrar el nombre del día
nombre = nombre_dia(numero_dia)
print("El día correspondiente es:", nombre)