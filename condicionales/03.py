import os 
os.system("cls")

def clasificar_angulo(grados):
  if grados == 0:
    return "Nulo"
  elif grados < 90:
    return "Agudo"
  elif grados == 90:
    return "Recto"
  elif grados < 180:
    return "Obtuso"
  elif grados == 180:
    return "Llano"
  else:
    return "Cóncavo o completo"

angulo = float(input("Ingrese el ángulo en grados: "))
print("El ángulo es:", clasificar_angulo(angulo))