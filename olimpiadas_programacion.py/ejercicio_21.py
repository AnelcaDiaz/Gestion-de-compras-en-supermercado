print("RONDA 1")
print("Ejercicio 23: Sistema de acceso por edad y membresia activa")

name=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
mem= input("Actualmente su membresia esta activa: ")

if edad>=18 and mem=="SI":
    print(f"usuario{name} puede acceder a los beneficios al cumplir con todos los requisitos")

else: print(f"usuario {name} ni puede acceder a los beneficios, ya que no cumple los requisitos")

