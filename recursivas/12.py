def invertir_cadena(cadena):
  """Invierte los caracteres de una cadena.

  Args:
    cadena: La cadena a invertir.

  Returns:
    La cadena invertida.
  """

  return cadena[::-1]

# Ejemplo de uso:
texto = "Hola mundo"
texto_invertido = invertir_cadena(texto)
print(texto_invertido)  # Salida: odnum aloH