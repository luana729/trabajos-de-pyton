import os
os.system

def encontrar_minimo_recursivo(vector, tamaño):
    if tamaño == 1:
         return vector[0]
    else:
         minimo_resto = encontrar_minimo_recursivo(vector[1:] , tamaño - 1)
    return min(vector[0] , minimo_resto)

# ejemplo de uso
mi_vector = [5, 2, 9, 1, 7]
tamaño = len(mi_vector)
resultado =  encontrar_minimo_recursivo(mi_vector , tamaño)
print("El numero mas pequeño es:" , resultado)
