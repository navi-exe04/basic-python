saludo = "Holaaa"  # variable global


def saludar():
    # si queremos hacer uso de variables globales tenemos que definir la palabra global
    global saludo
    saludo = "Hola mundo"  # variable local


def saludaChanchito():
    saludo = "Hola Chanchito"


print(saludo)
saludar()
print(saludo)
