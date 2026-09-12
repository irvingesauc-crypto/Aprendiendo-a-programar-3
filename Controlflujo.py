Edad=int(input("Ingrese su edad: "))
Faltante_para_100=100-Edad
if Edad<0 or Edad>120:
    print("Edad inválida. Por favor ingrese un valor entre 0 y 120.")
elif Edad<18:
    print(f"Tienes {Edad} años, eres menor de edad. Te faltan {Faltante_para_100} años para llegar a 100.")
else:
    print(f"Tienes {Edad} años, eres mayor de edad. Te faltan {Faltante_para_100} años para llegar a 100.")