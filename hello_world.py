a=(float(input("Ingrese coeficiente a:")))
b=(float(input("Ingrese coeficiente b:")))
c=(float(input("Ingrese coeficiente c:")))
Disc=b**2-4*a*c
if Disc>0:
    x1=(-b+(Disc**0.5))/(2*a)
    x2=(-b-(Disc**0.5))/(2*a)
    print("Las raices son reales y diferentes")
    print("x1=",x1)
    print("x2=",x2)
if Disc==0:
    x=(-b)/(2*a)
    print("Las raices son reales e iguales")
    print("x=",x)
if Disc<0:
    print("Las raices son complejas y diferentes")
