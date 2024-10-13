import os 
os.system("cls")

def calcular_porcentaje():
    while True:
       total = int(input("total de estudiantes:"))
       if total > 0:
           break
       print("El total de estudiantes debe ser mayor a cero.")
       
    while True:
        varones = int (input("numero de varones:"))
        if 0 <= varones <= total:
            break
        print(f"El numero de varones debe estar entre 0 y {total}.")
        
        mujeres = total - varones 
        print(f"porcentaje de varones:{(varones / total * 100): .2f}%")
        print(f"porcentaje de mujeres: {(mujeres / total * 100):.2f}%")

calcular_porcentaje()    

