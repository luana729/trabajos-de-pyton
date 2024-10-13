import os 
os.system("cls")

precio =  20 
unidades = int( input("Unidades :"))

compra = precio * unidades 

if  compra  <= 500 : descuento = 0.12 * compra 
elif compra <= 700 : descuento = 0.14 * compra 
else : descuento = 0.16 * compra 

print(f"Descuento = {compra: .2f}")
print(f"Descuento = {descuento: .2f}")
print(f"total = {(compra - descuento): .2f}")
print(f"caramelos = {caramelos: .2f}")