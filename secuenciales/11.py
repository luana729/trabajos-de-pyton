import os 
os.system("cls")

def intercambiar_cifras(num1, num2):
  a,  b, c = str(num1)
  d,  e, f = str(num2)
  return int(f+b+a) , int(c+e+d)

num1 =int(input("Ingrese el priemer numero de 3 cifras: "))
num2 = int(input("Ingrese el segundo numero de 3 cifras:  "))
print("Los numero con las cifras intercambiadas son:" , intercambiar_cifras(num1, num2))