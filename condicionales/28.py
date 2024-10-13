import os 
os.system("cls")

def hora24_a_12(hora):
    try:
        h, m = map(int, hora.split(':'))
        if not (0 <= h < 24 and 0 <= m < 60):
            return "Hora inválida"
        return f"{(h%12 or 12)}:{m:02d} {'PM' if h >= 12 else 'AM'}"
    except ValueError:
        return "Formato inválido"

hora = input("Hora (HH:MM): ")
print(hora24_a_12(hora))