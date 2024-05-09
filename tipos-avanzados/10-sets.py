# los sets son un grupo o conjuntos
# estos sets son como listas pero donde no muestra las datos repetidos
primer = {1, 1, 2, 2, 3, 4}
print(primer)

# podemos manipular los datos de los sets como las listas
# primer.add(5)
# primer.remove(1)
# print(primer)

# podemos crear un set en base a una lista o tupla
segundo = [3, 4, 5]
segundo = set(segundo)

# podemos unir los datos de dos sets con | (union)
print(primer | segundo)

# tambien se puede hacer interseccion entre dos sets con &
print(primer & segundo)

# tambien se puede calcular la diferencia entre sets con -
print(primer - segundo)

# diferencia simetrica con ^
print(primer ^ segundo)

# cuando se trata de sets, nosotros no podemos acceder a sus datos como con las listas normales
# solo podemos preguntar si el dato se encuentra en el set
if 5 in segundo:
    print("Hola mundo")
