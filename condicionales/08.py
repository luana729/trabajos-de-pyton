import os 
os.system("cls")

def calcular_propina(exámenes_aprobados):
  """Calcula el monto total de la propina.

  Args:
    exámenes_aprobados: Número de exámenes aprobados.

  Returns:
    El monto total de la propina.
  """

  propina_base = 20
  incentivo_por_examen = 5
  propina_adicional = exámenes_aprobados * incentivo_por_examen
  propina_total = propina_base + propina_adicional
  return propina_total

# Pedir al usuario que ingrese el número de exámenes aprobados
examenes_aprobados = int(input("Ingrese el número de exámenes aprobados: "))

# Calcular y mostrar la propina total
propina = calcular_propina(examenes_aprobados)
print("El monto total de la propina es: S/.", propina)