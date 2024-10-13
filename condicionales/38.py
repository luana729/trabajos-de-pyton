import os 
os.system("cls")

def es_bisiesto(año):
    """Verifica si un año es bisiesto."""
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def dias_en_mes(mes, año):
    """Devuelve el número de días en un mes específico de un año dado."""
    meses = {
        1: ("Enero", 31),
        2: ("Febrero", 29 if es_bisiesto(año) else 28),
        3: ("Marzo", 31),
        4: ("Abril", 30),
        5: ("Mayo", 31),
        6: ("Junio", 30),
        7: ("Julio", 31),
        8: ("Agosto", 31),
        9: ("Septiembre", 30),
        10: ("Octubre", 31),
        11: ("Noviembre", 30),
        12: ("Diciembre", 31)
    }
    return meses.get(mes, ("Mes inválido", 0))

def main():
    mes = int(input("Ingrese el número del mes (1-12): "))
    año = int(input("Ingrese el año: "))

    nombre_mes, dias = dias_en_mes(mes, año)

    if dias == 0:
        print("El mes ingresado no es válido.")
    else:
        print(f"Mes: {nombre_mes}, Días: {dias}")

if __name__ == "__main__":
    main()
