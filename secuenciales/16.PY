import os 
os.system("cls")

def calcular_sueldo(horas_trabajadas, tarifa_horaria):
  """Calcula el sueldo básico, bruto y neto de un trabajador.

  Args:
    horas_trabajadas: Número total de horas trabajadas.
    tarifa_horaria: Tarifa por hora trabajada.

  Returns:
    Una tupla con el sueldo básico, bruto y neto.
  """

  # Calcular el sueldo básico
  sueldo_basico = horas_trabajadas * tarifa_horaria

  # Calcular el sueldo bruto (sueldo básico + bonificación)
  bonificacion = sueldo_basico * 0.2
  sueldo_bruto = sueldo_basico + bonificacion

  # Calcular el sueldo neto (sueldo bruto - descuento)
  descuento = sueldo_bruto * 0.1
  sueldo_neto = sueldo_bruto - descuento

  return sueldo_basico, sueldo_bruto, sueldo_neto

# Solicitar al usuario los datos
horas = float(input("Ingrese el número de horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa horaria: "))

# Calcular los sueldos
basico, bruto, neto = calcular_sueldo(horas, tarifa)

# Mostrar los resultados
print("Sueldo básico:", basico)
print("Sueldo bruto:", bruto)
print("Sueldo neto:", neto)