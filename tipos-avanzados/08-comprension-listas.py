usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# podemos obtener los tipos de datos que queramos con la siguiente expresion
# expresion for item in items
# MAP
# nombres = [usuario[0] for usuario in usuarios]
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# filtrar usuarios que tengan un id mayor a 2
# FILTER
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
