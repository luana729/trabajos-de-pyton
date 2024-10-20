def invertir_caso(cadena):
  """Invierte el caso de cada letra en una cadena (mayúsculas a minúsculas y viceversa).

  Args:
    cadena: La cadena a modificar.

  Returns:
    La cadena con el caso invertido.
  """

  nueva_cadena = ""
  for caracter in cadena:
    if caracter.isupper():
      nueva_cadena += caracter.lower()
    else:
      nueva_cadena += caracter.upper()
  return nueva_cadena

# Ejemplo de uso:
texto = "HoLa, mUnDo!"
resultado = invertir_caso(texto)
print(resultado)  # Salida: hOlA, MuNdO!
