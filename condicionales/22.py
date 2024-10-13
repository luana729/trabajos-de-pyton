import os 
os.system("cls")

def costo_total(a, b):
    pa, pb = 25, 30
    da, db = 0.15 if a > 50 else 0, 0.1 if b > 60 else 0
    return (a * pa - a * pa * da) + (b * pb - b * pb * db)

a, b = int(input("A: ")), int(input("B: "))
print(f"Total: S/. {costo_total(a, b)}")