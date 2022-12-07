string= input("Introduzca una cadena de carácteres")
numeros="0123456789"
def localizarnum (string):
    contador=0
    for a in string:
        if a in numeros:
            contador=contador+1
    print ("De la cadena de carácteres introducidos ",contador," son números")
print (localizarnum (string))