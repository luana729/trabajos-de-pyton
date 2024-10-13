import os 
os.system("cls")

def determinar_tipo_empleado(codigo):
  """Determina el tipo de empleado según su código.

  Args:
    codigo: Un número entero de tres cifras.

  Returns:
    Una cadena con el tipo de empleado.
  """

  if codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0:
    return "Administrativo"
  elif codigo % 3 == 0 and codigo % 5 == 0:
    return "Directivo"
  elif codigo % 2 == 0:
    return "Vendedor"
  else:
    return "Seguridad"

# Solicitar el código al usuario
codigo = int(input("Ingrese el código del empleado: "))

# Determinar y mostrar el tipo de empleado
tipo_empleado = determinar_tipo_empleado(codigo)
print(f"El empleado con código {codigo} es de tipo: {tipo_empleado}")