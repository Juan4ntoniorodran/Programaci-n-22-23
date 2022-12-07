'''
Created on 3 dic 2022

@author: usuario
'''
cadena= input("Introduzca una cadena")
letra= input("Introduzca el carácter a revisar")

def repeticionescaracter (cadena, letra):
    repeticiones=0
    for i in cadena:
        if i==letra:
            repeticiones=repeticiones+1
    print (letra, "se repite en ",cadena,repeticiones,"veces")  
    
print (repeticionescaracter (cadena, letra))