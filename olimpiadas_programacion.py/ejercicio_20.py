
print("RONDA 2")
print("Clasificador de triangulo por angulos")

Ang1=int(input("Ingrese el primer angulo: "))
Ang2=int(input("Ingrese el segundo angulo:"))
Ang3=int(input("Ingrese el tercer angulo:"))
sum=Ang1+Ang2+Ang3

if sum==180:
    if Ang1==90 or Ang2==90 or Ang3==90:
        print("El triángulo es rectángulo")
        
    elif Ang1<90 and Ang2<90 and Ang3<90:
        print("El triangulo es ocutángulo")
        
    else:
        print("El triangulo es obtusángulo")
        
else:
    print(f"La suma de sus angulos {Ang1}{Ang2}{Ang3} no suman 180 grados, así que no es un triángulo")
    