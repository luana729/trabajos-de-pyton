import os 
os.system("cls")

def convertir_metros(metros):
    """convierte metros  a cm, pulgadas, pies y yardas."""

    cm= metros * 100
    pulgadas = cm / 2.54
    pies = pulgadas / 12
    yardas = pies / 3
    return f"{metros} metros equivalem a:\n{cm:.2f}  cm\n{pulgadas:.2f} pulgadas\n{pies} pies\n{yardas:.2f} yardas"

metros = float(input("Ingrese metros:"  ))
print(convertir_metros(metros))

