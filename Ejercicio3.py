'''
Created on 4 dic 2022

@author: usuario
'''
cadena= input("Introduzca una cadena de carácteres")

def uppercaseinstring (cadena):
    contador=0
    for i in cadena:
        if i==i.upper():
            contador=contador+1
    print ("Hay ",contador," mayúsculas en la cadena introducida")

print(uppercaseinstring(cadena))