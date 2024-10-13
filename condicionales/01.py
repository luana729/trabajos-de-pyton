import os 
os.system("cls")

def calcular_compra(cantidad):
    """Calcula el importe total de una compra con descuentos por cantidad.

    Args:
        cantidad: Número de unidades compradas.

    Returns:
        El importe total a pagar.
    """

    # Precios unitarios por rangos de cantidad
    precios = {
        range(1, 26): 27,  # 1 a 25 unidades
        range(26, 51): 25,  # 26 a 50 unidades
        range(51, float('inf')): 23  # 51 unidades o más
    }

    # Obtener el precio unitario correspondiente al rango de cantidad
    precio_unitario = next(precio for rango, precio in precios.items() if cantidad in rango)

    # Calcular el importe total antes del descuento
    importe_total = cantidad * precio_unitario

    # Aplicar el descuento según la cantidad
    descuento = importe_total * (0.15 if cantidad > 50 else 0.05)

    # Calcular el importe total a pagar
    total_a_pagar = importe_total - descuento

    return total_a_pagar

# Solicitar la cantidad de unidades al usuario
cantidad_unidades = int(input("Ingrese la cantidad de unidades: "))

# Calcular el importe total y mostrarlo
total = calcular_compra(cantidad_unidades)
print(f"El total a pagar es: S/. {total:.2f}")