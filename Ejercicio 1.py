# 1.
from random import randint

lista=[]
listaaux=[]

while len(lista)<100:
    numero= randint(0,99)
    lista.append(numero)

def mayor (lista):
    mayor=lista[0]
    for i in lista:
        if i>mayor:
            mayor=i
    print (mayor)
    return

def menor (lista):
    menor=lista[0]
    for i in lista:
        if i<menor:
            menor=i
    print (menor)
    return

def sumarvalores (lista):
    suma=0
    for numero in lista:
        suma+=numero
    print (suma)
    return 

def media (lista):
    media=0
    media=sumarvalores(lista)/len(lista)
    print (media)
    return 

def sustituir (lista):
    posicion=int(input("Introduzca la posición del valor que desea reemplazar"))
    nuevovalor=int(input("Introduzca el nuevo valor"))
    lista[posicion]=nuevovalor
    print (lista)
    return

opcion=input("Introduzca la opción a ejecutar")

while opcion!="Mayor" and opcion!="Menor" and opcion!="Suma" and opcion!="Media" and opcion!="Sustituir" and opcion!="Mostrar":
    opcion= input("Por favor, introduzca una opción válida")

if opcion=="Mayor":
    nummayor=mayor(lista)
elif opcion=="Menor":
    nummenor=menor(lista)
elif opcion=="Suma":
    sumval=sumarvalores(lista)
elif opcion=="Media":
    mediaval=media(lista)
elif opcion=="Sustituir":
    sustituto=sustituir(lista)
elif opcion=="Mostrar":
    print (lista)

