'''
Created on 25 nov 2022

@author: usuario
'''
meses= ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
dias= [31,28,31,30,31,30,31,31,30,31,30,31]

mes= input("Introduzca un mes")

while mes not in meses:
    mes= input("Introduzca un valor correcto")

año= int(input("Introduzca un año"))

while año<0:
    año= int(input("Introduzca un año válido"))
    
def isleapyear (año):
    if año%4==0:
        return True
    elif año%100==0 and año%400==0:
        return True
    else:
        return False

print (isleapyear(año))

def computeDaysinMonth (mes):
    if mes=="Enero" or mes=="Marzo" or mes=="Mayo" or mes=="Julio" or mes=="Agosto" or mes=="Octubre" or mes=="Diciembre":
        return 31
    elif mes=="Abril" or mes=="Junio" or mes=="Septiembre" or mes=="Noviembre":
        return 30
    elif mes=="Febrero":
        if isleapyear(año)==True:
            return 29
        else:
            return 28
    else:
        return -1
    
print (computeDaysinMonth(mes))
    
    
    
    
    
    
    
    
    