'''
Created on 4 dic 2022

@author: usuario
'''
cadena= input("Introduzca una cadena de texto")
palabra= input("Introduzca la palabra que desea encontrar dentro de la cadena introducida")

def hiddenword (cadena, palabra):
    word=[]
    contador=0
    for a in palabra:
        for b in cadena:
           if a==b and b not in word:
               word.append(b)
    for i in word:
        if i in palabra:
            contador=contador+1
        else:
            contador=contador
    if contador==len(palabra):
        return True
    else:
        return False
print (hiddenword(cadena,palabra))