year= int(input("Introduzca un año"))

def isleapyear (year):
    if year%4==0:
        return True
    elif year%100==0 and year%400==0:
        return True
    else:
        return False

print (isleapyear(year))