import os 
os.system("cls")

# Sueldo básico
sueldo_basico = 250

# Leer el monto total vendido
monto_vendido = float(input("Ingrese el monto total vendido: "))

# Calcular comisión
comision = (monto_vendido * 0.05 if monto_vendido < 5000 else
            monto_vendido * 0.08 if monto_vendido < 10000 else
            monto_vendido * 0.10 if monto_vendido < 20000 else
            monto_vendido * 0.15)

# Calcular sueldo bruto y neto
sueldo_bruto = sueldo_basico + comision
descuento = sueldo_bruto * (0.15 if sueldo_bruto > 3500 else 0.08)
sueldo_neto = sueldo_bruto - descuento

# Mostrar resultados
print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}\nComisión: S/. {comision:.2f}\nDescuento: S/. {descuento:.2f}\nSueldo neto: S/. {sueldo_neto:.2f}")
