'''
Created on 22 nov 2022

@author: usuario
'''
cadena= input("Introduzca una cadena de texto")
lista=[]
lista.append(cadena)

while len(lista)<5:
    cadena= input("Introduzca una cadena de texto")
    lista.append(cadena)
    
def cadenamayor (lista):
    mayor=""
    for i in lista:
        if len(i)>len(i+1):
            mayor=i
    return mayor

