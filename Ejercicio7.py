'''
Created on 27 nov 2022

@author: usuario
'''
num= int(input("Introduzca un número"))

def isPrime (num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
print (isPrime(num))