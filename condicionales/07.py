import os 
os.system("cls")

def intermedio(a, b, c):
    return sorted([a, b, c])[1]

num1 =int(input("numero 1: "))
num2 = int(input("numero 2: "))
num3 = int(input("numero 3: "))
print("El numero intermedio es:",intermedio(num1, num2, num3))

