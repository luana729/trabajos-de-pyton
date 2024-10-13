import os 
os.system("cls")

def determinar_signo(numero):
  """Determina si un número es positivo, negativo o cero.

  Args:
    numero: El número a evaluar.

  Returns:
    Una cadena indicando el signo del número.
  """

  if numero > 0:
    return "positivo"
  elif numero < 0:
    return "negativo"
  else:
    return "cero"

# Pedir al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Determinar y mostrar el signo
signo = determinar_signo(numero)
print(f"El número {numero} es {signo}.")