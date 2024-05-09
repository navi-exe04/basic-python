# la palabra def nos ayuda a establecer a una funcion
# parametro es el dato que va a recibir la funcion
# podemos definir valores por defecto a los parametros en caso de que no se defina el argumento en la funcion
def hola(nombre, apellido="Feliz"):
    print("hola mundo")
    print(f"Bienvenido {nombre} {apellido}")


# argumentos son los valores que se el esta pasando a una funcion
hola("Raul")

# podemos definir el parametro al cual pertenece el argumento para que no vaya en un orden especifico
hola(apellido="Langle", nombre="Raul")
