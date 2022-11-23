'''
Created on 22 nov 2022

@author: usuario
'''
numero= int(input("Introduzca un número"))
lista=[]

lista.append(numero)

while len(lista)<10:
    numero= int(input("Introduzca un número"))
    lista.append(numero)
    
print ("***************************")
print ("Opciones a realizar con la lista de dígitos introducidos: ")
print ("a) Mostrar numeros menores a un número x")
print ("b) Mostrar numeros mayores a un número x")
print ("c) Mostrar los números que sean múltiplos de x")
print ("***************************")

opcion= input("¿Qué opción elige?")

while opcion!="a" and opcion!="b" and opcion!="c":
    opcion= input("Por favor,introduzca una de las opciones anteriormente presentadas")

x= int(input("Introduzca el número x"))
    
def menores (lista):
    listamenor=[]
    for i in lista:
        if i<x:
            listamenor.append(i)
    print (listamenor)
    return

def mayores (lista):
    listamayor=[]
    for i in lista:
        if i>x:
            listamayor.append(i)
    print (listamayor)
    return

def multiplos (lista):
    listamultiplos=[]
    for i in lista:
        if i%x==0:
            listamultiplos.append(i)
    print (listamultiplos)
    return

if opcion=="a":
    print (menores(lista))
elif opcion=="b":
    print (mayores(lista))
elif opcion=="c":
    print (multiplos(lista))
    
    
    
    
    
    
    