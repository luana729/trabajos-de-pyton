import os 
os.system("cls")

def compra(docenas, precio):
    desc = 0.15 if docenas >= 30 else 0.10 if docenas >= 6 else 0
    regalo = docenas // 3 if docenas >= 30 else 0
    total = docenas * precio * (1-desc)
    return total, desc, regalo

docenas = int(input("Docenas: "))
precio = float(input("Precio/docena: "))
total, desc, regalo = compra(docenas, precio)
print(f"Total: S/.{total:.2f}, Descuento: {desc*100:.2f}%, Regalos: {regalo}")