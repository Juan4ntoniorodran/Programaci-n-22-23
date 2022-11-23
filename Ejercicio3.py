'''
Created on 20 nov 2022

@author: usuario
'''
dia= int(input("Introduzca el día"))
mes= int(input("Introduzca el mes"))
año= int(input("Introduzca el año"))

while dia>31:
    dia= int(input("Introduzca un día válido"))

while mes>12 or mes<1:
    mes= int(input("Introduzca un mes válido"))
    
while dia>28 and mes==2:
    dia= int(input("Introduzca un día válido"))
    
def fechalarga (dia, mes, año):
    meses= ["Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    if mes==1:
        mes=meses[0]
    elif mes==2:
        mes=meses[1]
    elif mes==3:
        mes=meses[2]
    elif mes==4:
        mes=meses[3]
    elif mes==5:
        mes=meses[4]
    elif mes==6:
        mes=meses[5]
    elif mes==7:
        mes=meses[6]
    elif mes==8:
        mes=meses[7]
    elif mes==9:
        mes=meses[8]
    elif mes==10:
        mes=meses[9]
    elif mes==11:
        mes=meses[10]
    else:
        mes=meses[11]
        
    print (dia," de ",mes," del ",año)
    return
fechalarga= str(fechalarga(dia, mes, año))
print (fechalarga)