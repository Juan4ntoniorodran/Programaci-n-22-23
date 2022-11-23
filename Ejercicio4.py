'''
Created on 21 nov 2022

@author: usuario
'''
numero= int(input("Introduzca un número"))
lista=[]
lista.append(numero)

while numero>=0:
    numero=int(input("Introduzca un número"))
    lista.append(numero)
    
def mayor (lista):
    mayor=lista[0]
    for i in lista:
        if i>mayor:
            mayor=i
    print ("El mayor valor de la lista es: ",mayor)
    

def pares (lista):
    listapares=[]
    for i in lista:
        if i%2==0:
            listapares.append(i)
    print ("Estos son los números pares de la lista: ",listapares)
    
mayor=mayor(lista)
pares=pares(lista)
print(mayor)
print(pares)