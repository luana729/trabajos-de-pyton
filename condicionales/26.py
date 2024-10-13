import os 
os.system("cls")

def pagos(monto):
  porc = 0.3 if monto > 5000 else 0.2
  prestamo = monto * porc
  return monto - prestamo, prestamo * 1.1

monto = float(input("Monto: "))
pago, total_prestamo = pagos(monto)
print(f"Pago empresa: ${pago:.2f}\nPréstamo total: ${total_prestamo:.2f}")