import os
os.system

def suma_matriz_recursiva(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    if filas == 1 and columnas == 1:
        return matriz[0] [0]
    else:
        suma = sum(matriz[0]) # suma la primera fila
        return suma + suma_matriz_recursiva(matriz[1:])
    
# ejemplo de uso
matriz = [[1, 2, 3] , [4, 5, 6] , [7, 8, 9]]
resultado = suma_matriz_recursiva(matriz)
print("la suma de los elementos de la matriz es:" , resultado)
                                            