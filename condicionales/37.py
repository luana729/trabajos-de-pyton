import os 
os.system("cls")

def elegir_presidenta(pamela, carol, fanny):
    """Determina el resultado de una elección.

    Args:
        pamela: Votos de Pamela.
        carol: Votos de Carol.
        fanny: Votos de Fanny.

    Returns:
        El resultado de la elección.
    """

    total = pamela + carol + fanny
    necesario = total // 2 + 1
    if pamela == carol == fanny: return "Empate triple"
    if pamela >= necesario: return "Gana Pamela"
    if carol >= necesario: return "Gana Carol"
    if fanny >= necesario: return "Gana Fanny"
    primero, segundo = sorted([pamela, carol, fanny], reverse=True)[:2]
    if primero == segundo: return "Empate en segundo lugar"
    return "Segunda vuelta"

# Solicitar votos
pamela = int(input("Votos Pamela: "))
carol = int(input("Votos Carol: "))
fanny = int(input("Votos Fanny: "))

# Mostrar resultado
print(elegir_presidenta(pamela, carol, fanny))