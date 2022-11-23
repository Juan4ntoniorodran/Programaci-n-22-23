'''
Created on 22 nov 2022

@author: usuario
'''
lista1=[]

numero= int(input("Introduzca un número"))
lista1.append(numero)

while len(lista1)<10:
    numero= int(input("Introduzca un número"))
    lista1.append(numero)

lista2=[]

numero2= int(input("Introduzca un número"))
lista2.append(numero2)

while len(lista2)<10:
    numero2= int(input("Introduzca un número"))
    lista2.append(numero2)
    
def intersect (lista1,lista2):
    listacomunes=[]
    for i in lista1:
        if (i not in listacomunes) and (i in lista2):
            listacomunes.append(i)
    return (listacomunes)

print (intersect(lista1,lista2))