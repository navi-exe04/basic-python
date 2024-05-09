numeros = [4, 1, 10, 8, 5, 22, 75]

# numeros.sort()  # ordena los elementos de la lista
# numeros.sort(reverse=True)  # ordena los elementos de la lista en reversa

# ordena los elementos de la lista para crear una nueva
numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)

# solo se pueden ordenar datos iterables
# usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]
# usuarios.sort()
# print(usuarios)

usuarios2 = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]


# def ordena(elemento):
#     return elemento[1]  # regresa el dato a ordenar de la lista


# las funciones lambda permiten establecer funciones anonimas
usuarios2.sort(key=lambda el: el[1])
print(usuarios2)
