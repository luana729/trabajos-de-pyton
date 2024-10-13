import os 
os.system("cls")

def categoria(sexo, edad):
    return 'F' + ('A' if edad < 23 else 'B') if sexo == 'F' else 'M' + ('A' if edad < 25 else 'B')

sexo = input("Sexo (F/M): ").upper()
edad = int(input("Edad: "))
print(f"Categoría: {categoria(sexo, edad)}")