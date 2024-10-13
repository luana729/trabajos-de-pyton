import os 
os.system("cls")

def calcular_imc(peso, estatura):
    """Calcula el índice de masa corporal (IMC) de una persona.

    Args:
        peso: Peso de la persona en kilogramos.
        estatura: Estatura de la persona en metros.

    Returns:
        El valor del IMC y una descripción del grado de obesidad.
    """

    imc = peso / (estatura ** 2)

    if imc < 20:
        return imc, "Delgado"
    elif imc < 25:
        return imc, "Normal"
    elif imc < 27:
        return imc, "Sobrepeso"
    else:
        return imc, "Obesidad"

# Solicitar datos al usuario
peso = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Calcular el IMC y mostrar el resultado
imc, grado_obesidad = calcular_imc(peso, estatura)
print(f"Tu IMC es: {imc:.2f}")
print(f"Grado de obesidad: {grado_obesidad}")