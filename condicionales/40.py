import os 
os.system("cls")

def calcular_promedio(pc1, pc2, pc3, ep, ef, pesos):
  """Calcula el promedio final de un curso.

  Args:
    pc1: Nota de la primera práctica.
    pc2: Nota de la segunda práctica.
    pc3: Nota de la tercera práctica.
    ep: Nota del examen parcial.
    ef: Nota del examen final.
    pesos: Lista con los pesos de cada evaluación.

  Returns:
    El promedio final del curso.
  """

  promedio = (pc1 * pesos[0] + pc2 * pesos[1] + pc3 * pesos[2] + ep * pesos[3] + ef * pesos[4]) / 100
  return promedio

def evaluar_curso(promedio):
  """Evalúa si un estudiante aprobó o desaprobó el curso.

  Args:
    promedio: El promedio final del curso.

  Returns:
    "Aprobado" si el promedio es mayor o igual a 13, "Desaprobado" en caso contrario.
  """

  return "Aprobado" if promedio >= 13 else "Desaprobado"

# Pesos de cada curso
pesos_matematica = [10, 20, 10, 30, 30]
pesos_fisica = [20, 20, 20, 20, 20]
pesos_quimica = [10, 30, 10, 25, 25]

# Solicitar notas al usuario
curso = input("Ingrese el curso (Matemática, Física o Química): ")
pc1 = float(input("Ingrese la nota de la primera práctica: "))
pc2 = float(input("Ingrese la nota de la segunda práctica: "))
pc3 = float(input("Ingrese la nota de la tercera práctica: "))
ep = float(input("Ingrese la nota del examen parcial: "))
ef = float(input("Ingrese la nota del examen final: "))

# Seleccionar los pesos según el curso
if curso.lower() == "matemática":
  pesos = pesos_matematica
elif curso.lower() == "física":
  pesos = pesos_fisica
else:
  pesos = pesos_quimica

# Calcular el promedio y evaluar el curso
promedio_final = calcular_promedio(pc1, pc2, pc3, ep, ef, pesos)
resultado = evaluar_curso(promedio_final)

# Mostrar el resultado
print(f"El promedio final en {curso} es: {promedio_final}")
print(f"El estudiante está {resultado}.")