print("Ejercicio 13: Gestion de compras en supermercado")

#Creamos las listas, e interactuamos con el usuario, pidiendo que agregue a la lista de productos y clientes

clientes = ["Alejandra", "Fernando", "Natalia"]
clientes.append(input("Ingrese un nombre del cliente: "))
clientes.append(input("Ingrese un nombre del cliente: "))

productos = ["Arroz", "Leche", "Huevos"]
productos.append(input("Ingrese un producto: "))
productos.append(input("Ingrese un producto: "))

#In: Sirve para especificar "en" dentro de un texto

if "Natalia" in clientes:
    clientes.append("Carlos")
    print(f"La lista es {clientes}")
    
else:
    print("No se cumplio la condicion")

if "Huevos" in productos:
        productos.append("Pan")
        print(f"La lista actualizada es {productos}")
else:
    print("No se cumplio la condicion")

if"Fernando" in clientes:
            clientes.remove("Fernando")

else:
    print("No se cumplio la condicion")

if len(productos)>3:
    productos.remove("Arroz")
    print(f"la lista actualizada es{productos}")
    
    
if "Alejandra" in clientes:
    clientes.remove("Alejandra")
    clientes.append("Marcela")
    print(f"la lista actualizada es {clientes}")
    
    
turno_caja= clientes[:2]

canasta_basica=productos[-2:]

if "pan" in canasta_basica:
    producto_oferta= ("pan", 2500)
    
else:
    print("No se cumple la condicion")
    
#Crear diccionario si hay "preferencial"    
    
if "preferencial" in turno_caja:
    venta= {
    "cliente": "Marcela",
    "producto": "Leche",
    "total": 3500
    }

else:
    print("No se encuentra el diccionario")
    
#Añadir medio de pago solo si venta existe
#Equivale a if len(venta)>0

if "venta" in locals():
    venta["medio de pago"]= "Tarjeta debito"

else:
    print("No se cumplio la condicion")
if "Azucar" not in productos:
    productos.append("Azucar")
    
else:
    print("No se cumplio la condicion")

if "Fernando" not in clientes:
    clientes.append("Fernando")
    
else:
    print("No se cumplio la condicion")

#Muestra en las listas  clientes, productos, turno_caja, canasta_basica, cualquier tupla creada y el diccionario venta si fue creado

print(f"Lista clientes{clientes}")

print(f"Lista de productos {productos}")

print(f"Lista de el turno de caja {turno_caja}")

print(f"Lista de la canasta básica {canasta_basica}")

