nota1=int(input("ingresar n1:"))
nota2=int(input("ingresar n2:"))
nota3=int(input("ingresar n3:"))
nota4=int(input("ingresar n4:"))

promedio=(nota1+nota2+nota3+nota4)/4
if promedio>100:
    print ("error")
   
elif promedio>89 and promedio <101:
    print("A")
elif promedio>79 and promedio< 90:
    print("B")
elif promedio>69 and promedio< 80:
    print("C")
elif promedio>59 and promedio< 70:
    print("D")

elif promedio>=0 and promedio<60:
    print("E")
