import os 
os.system("cls")

def convertir_gigabytes(gigabytes):
    return gb * 1024, gb * 1024**2, gb *1024**3

    

# Solicitar la cantidad de gigabytes al usuario 
gigabytes = float(input("Ingrese la cantidad del disco duro en gigabytes: "))

# mostrar los resultados 

gb = float(input("GB:"))
mb, kb, b = convertir_gigabytes("gigabytes")
print(f"MB: {mb: .2f}, KB: {kb:2f} ,B: {b: .2f}")
