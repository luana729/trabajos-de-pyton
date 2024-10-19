import os
os.system

def division_por_restas(dividendo, divisor):
    # caso base: si el dividendo  es menor que el divisor, el cociente es 0 y el residuo es el dividendo 
    if dividendo < divisor:
        return ( 0, dividendo)
    else:
        # llamada recursiva, restando el divisor al dividendo 
        cociente, residuo = division_por_restas(dividendo - divisor, divisor )
        return (cociente + 1, residuo)
    
         # ejemplo de uso 
dividendo = 10
divisor = 3
cociente, residuo = division_por_restas(dividendo , divisor)
print(f"la divison es { dividendo} entre {divisor} de  un cociente de {cociente} y un residuo de {residuo}.")