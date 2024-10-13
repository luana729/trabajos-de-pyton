import os 
os.system("cls")

def calcular_lapiceros(cuadernos):
    """Calcula la cantidad de lapiceros obsequiados según la cantidad de cuadernos adquiridos."""
    # Inicializar contadores de lapiceros
    lucas = 0
    faber = 0
    pilot = 0

    # Determinar la cantidad de lapiceros según la cantidad de cuadernos
    if cuadernos < 12:
        return lucas, faber, pilot  # No se obsequia ningún lapicero
    elif 12 <= cuadernos < 24:
        lucas = cuadernos // 4  # 1 Lucas por cada 4 cuadernos
    elif 24 <= cuadernos < 36:
        faber = (cuadernos // 4) * 2  # 2 Faber por cada 4 cuadernos
    else:  # 36 o más cuadernos
        pilot = (cuadernos // 4) * 2  # 2 Pilot por cada 4 cuadernos
        faber = cuadernos // 6  # 1 Faber por cada 6 cuadernos
        lucas = cuadernos // 12  # 1 Lucas por cada 12 cuadernos

    return lucas, faber, pilot

def main():
    # Solicitar al usuario el número de cuadernos
    cuadernos = int(input("Ingrese el número de cuadernos adquiridos: "))

    # Calcular la cantidad de lapiceros
    lucas, faber, pilot = calcular_lapiceros(cuadernos)

    # Mostrar resultados
    print(f"\nNúmero de cuadernos adquiridos: {cuadernos}")
    print(f"Lapiceros Lucas: {lucas}")
    print(f"Lapiceros Faber: {faber}")
    print(f"Lapiceros Pilot: {pilot}")

if __name__ == "__main__":
    main()
