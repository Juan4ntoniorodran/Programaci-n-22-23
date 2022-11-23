ficha1=[]

num= int(input("Introduzca el valor de un lado de la ficha"))
while num>6 or num<1:
    num= int(input("Introduzca un número válido"))
ficha1.append(num)
num2= int(input("Introduzca el valor del otro lado de la ficha"))
while num2>6 or num2<1:
    num2= int(input("Introduzca un número válido"))
ficha1.append(num2)

ficha2=[]

num3= int(input("Introduzca el valor de un lado de la ficha"))
while num3>6 or num3<1:
    num3= int(input("Introduzca un número válido"))
ficha2.append(num3)
num4= int(input("Introduzca el valor del otro lado de la ficha"))
while num4>6 or num4<1:
    num4= int(input("Introduzca un número válido"))
ficha2.append(num4)

def encajan (ficha1,ficha2):
    if ficha1[1]==ficha2[1] or ficha1[0]==ficha2[0]:
        print ("Las fichas encajan")
    else:
        print ("Las fichas no encajan")

print (encajan(ficha1,ficha2))
