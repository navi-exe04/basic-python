mascotas = ["Wolfbang", "Pelusa", "Pulga", "Copito"]

# podemos iterar las listas con for
for mascota in mascotas:
    print(mascota)

# la palabra enumerate nos permite observar una tupla de los datos de la lista
for mascota in enumerate(mascotas):
    print(mascota)  # podemos acceder a la tupla
    print(mascota[0])  # accedemos al indice de la lista
    print(mascota[1])  # accedemos al valor de la lista

# tambien podemos acceder al indice de la lista especificando su nombre al principio
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
