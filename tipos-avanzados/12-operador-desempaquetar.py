lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

# el * nos permite desempaquetar los datos de listas o tuplas
print(*lista1)
combinada = ["Hola", *lista1, "Mundo", *lista2]
print(combinada)


# tambien podemos desempaquetar datos de un diccionario con **
punto1 = {"x": 19}
punto2 = {"y": 20}
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
