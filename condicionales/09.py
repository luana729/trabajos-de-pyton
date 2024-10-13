import os 
os.system("cls")

def descuento(codigo, cantidad):
  precios = {101: 17, 102: 25, 103: 16, 104: 27}
  descuentos = {101: (1, 10, 5), 102: (11, 20, 8), 103: (21, 30, 10), 104: (31, float('inf'), 13)}
  
  precio = precios.get(codigo, 0)
  if precio == 0:
    return "Código inválido"
  
  min_cant, max_cant, desc = descuentos[codigo]
  if min_cant <= cantidad <= max_cant:
    descuento = precio * cantidad * desc / 100
  else:
    descuento = 0
  
  total = precio * cantidad - descuento
  return total

codigo = int(input("Código: "))
cantidad = int(input("Cantidad: "))
print("Total a pagar:", descuento(codigo, cantidad))