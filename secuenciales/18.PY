import os 
os.system("cls")

def descuento_doble(cantidad, precio):
    total = cantidad * precio
    descuento = total * 0.15
    return total, descuento, total - descuento * 1.15

cantidad =int(input("cantidad: "))
precio = float(input("precio unitario: "))
inicial, descuento, final = descuento_doble(cantidad,  precio)
print(f"Total: ${inicial: .2f}, Descuento: ${descuento: .2f}), Final: ${final: .2f} ")