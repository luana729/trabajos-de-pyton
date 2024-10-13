import os 
os.system("cls")

from statistics import mean

# Pedimos al usuario que ingrese 5 numeros y las almacenamos en una lista 
numeros = [float(input(f"Ingrese el numero  {i+1}:")) for i in range(5)]

# Ordenamos los numeros de mayores a menor 
numeros_ordenados = sorted(numeros, reverse=True)

# Calculamos el promedio de los 3 primeros (los mayores)
promedio = mean(numeros_ordenados[:3])

# Imprimimos el resultado
print("El promedio de los 3 numeros mayores es:", promedio)


 
  
 
