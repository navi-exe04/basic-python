mascotas = ["Wolfbang", "Pelusa", "Pulga", "Copito", "Pelusa"]

mascotas.insert(1, "Melvin")  # Permite insentar un dato en cierto indice
mascotas.append("Chanchito triste")  # Agrega un dato al final de la lista

# remueve un elemento de la lista (solo 1 el primero que encuentre)
mascotas.remove("Pelusa")
# remueve el ultimo elemento de la lista
mascotas.pop()  # tambien podemos especificar el indice del elemento

del mascotas[0]  # tambien se pueden eliminar elementos con del y el indice

mascotas.clear()  # eliminamos todo el contenido de la lista

print(mascotas)
