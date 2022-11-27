'''
Created on 27 nov 2022

@author: usuario
'''
base= int(input("Introduzca un número"))

exponente= int(input("Introduzca otro número"))

def powerit(base, exponente):
    potencia=base
    if exponente==0:
        return 1
    else:
        for i in range (1,exponente):
            potencia=potencia*base
    return potencia
  
print (powerit(base,exponente))  