# coleccion de datos agrupados por una llave y un valor
punto = {"x": 25, "y": 50}  # las llaves solo pueden ser string

print(punto)

# para acceder a un dato debemos especificar el string de la llave
print(punto["x"])
print(punto["y"])

# podemos definir nuevos valores para el diccionario
punto["z"] = 10
print(punto)

# si no se encuentra algun valor lo podemos comprobar con un if
if "lala" in punto:
    print("encontre a lala", punto["lala"])

# tambien se pueden obtener datos con .get, en caso de que no exista, regresa none
print(punto.get("x"))
# se puede regresar un valor por defecto en caso de que no exista
print(punto.get("lala", 97))

# podemos eliminar valores con del y su llave
del punto["x"]
del punto["y"]
print(punto)

# podemos iterar todos los datos del diccionario con for
punto["x"] = 25

# for valor in punto:
#     print(valor, punto[valor])

for llave, valor in punto.items():  # .items() regresa una tupla
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"}
]

for usuario in usuarios:
    print(usuario["nombre"])
