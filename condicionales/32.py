import os 
os.system("cls")

def calcular_pension(categoria, promedio, pension_base):
    """
    Calcula la nueva pensión de un estudiante.

    Args:
        categoria: La categoría del estudiante (A, B, C o D).
        promedio: El promedio ponderado del ciclo anterior.
        pension_base: La pensión base de la categoría.

    Returns:
        Un diccionario con la pensión base, el descuento y la nueva pensión.
    """

    descuentos = {
        'A': (0, 13.99, 0),
        'B': (14, 15.99, 10),
        'C': (16, 17.99, 12),
        'D': (18, 20, 15)
    }
    min_prom, max_prom, descuento = descuentos[categoria]

    if min_prom <= promedio <= max_prom:
        nueva_pension = pension_base * (1 - descuento / 100)
    else:
        nueva_pension = pension_base

    return {
        'Pensión Base': pension_base,
        'Descuento': descuento,
        'Nueva Pensión': nueva_pension
    }

# Solicitar datos al usuario
categoria = input("Ingrese la categoría del estudiante (A, B, C o D): ").upper()
promedio = float(input("Ingrese el promedio ponderado del ciclo anterior: "))

# Obtener la pensión base según la categoría
pensiones = {'A': 550, 'B': 500, 'C': 450, 'D': 400}
pension_base = pensiones[categoria]

# Calcular la nueva pensión
resultado = calcular_pension(categoria, promedio, pension_base)

# Mostrar el resultado
print("Pensión Base: S/.", resultado['Pensión Base'])
print("Descuento: {}%".format(resultado['Descuento']))
print("Nueva Pensión: S/.", resultado['Nueva Pensión'])