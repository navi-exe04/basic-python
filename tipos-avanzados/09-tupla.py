# es una lista que no puede ser editada
# esta hecho para listas que tienen datos que no pueden ser manipulables
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# el metodo tuple convierta en tupla cualquier dato iterable
punto = tuple([1, 2])
print(punto)

# podemos acceder a los datos de la tupla
menosNumeros = numeros[:2]
print(menosNumeros)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

# en caso de querer manipular los datos de la dupla, lo mejor es crear
# una nueva lista con los datos de la tupla
lista = list(numeros)
lista[1] = 10
print(lista)
