import os 
os.system("cls")

def calcular_eficiencia(ausencias, defectuosos, no_defectuosos):
  """Calcula el grado de eficiencia de un operario de torno.

  Args:
    ausencias: Número de horas de ausencia.
    defectuosos: Número de tornillos defectuosos.
    no_defectuosos: Número de tornillos no defectuosos.

  Returns:
    El grado de eficiencia del operario.
  """

  # Condiciones para cada grado
  condiciones = [
    ausencias <= 1.5,  # Condición 1
    defectuosos < 300, # Condición 2
    no_defectuosos > 10000 # Condición 3
  ]

  # Asignación de grados según las condiciones
  if not any(condiciones):
    return 5
  elif condiciones[0] and condiciones[1]:
    return 12
  elif condiciones[0] and condiciones[2]:
    return 13
  elif condiciones[1] and condiciones[2]:
    return 15
  elif condiciones[0]:
    return 7
  elif condiciones[1]:
    return 8
  else:
    return 9

# Solicitar datos al usuario
ausencias = float(input("Ingrese el número de horas de ausencia: "))
defectuosos = int(input("Ingrese el número de tornillos defectuosos: "))
no_defectuosos = int(input("Ingrese el número de tornillos no defectuosos: "))

# Calcular y mostrar el grado de eficiencia
eficiencia = calcular_eficiencia(ausencias, defectuosos, no_defectuosos)
print("El grado de eficiencia del operario es:", eficiencia)