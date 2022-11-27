'''
Created on 27 nov 2022

@author: usuario
'''
num= int(input("Introduzca un número"))
numeros=[]
def getNumberofDigits (num):
    for i in range(0,num):
        numeros.append(i)
    return numeros
print (getNumberofDigits(num))