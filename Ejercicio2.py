'''
Created on 3 dic 2022

@author: usuario
'''
cadena= input("Introduzca una cadena de carácteres")

def lowcaseinstring (cadena):
    contador=0
    for i in cadena:
        if i==i.lower():
            contador=contador+1
    print ("Hay ",contador," minúsculas en la cadena introducida")

print(lowcaseinstring(cadena))            