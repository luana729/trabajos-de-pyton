import os 
os.system("cls")


def aportes(j, r, d):
    total = j + r + d/3
    return total, (j/total)*100, (r/total)*100, (d/total)*100

juan = float(input("Juan (USD): "))
rosa = float(input("Rosa (USD): "))
daniel = float(input("Daniel (soles): "))

total, p_juan, p_rosa, p_daniel = aportes(juan, rosa, daniel)

print(f"Total: ${total}")
print(f"juan:{p_juan: .2f}%")
print(f"Rosa: {p_rosa: .2f}%")
print(f"Daniel: {p_daniel: .2f}%")