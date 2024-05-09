animal = " cerdito fEliz "

# los string tienen distintos metodos para manipularlos
print(animal.upper())  # convierte el string a mayusculas
print(animal.lower())  # convierte el string a minusculas
# Da formato a string para que la primera letra sea mayuscula
print(animal.capitalize())
# Da formato para hacer la primera letra de cada palabra en mayuscula
print(animal.title())
print(animal.strip())  # remueve los espacios en blanco a la izquierda y derecha
print(animal.strip().capitalize())  # Podemos encadenar los metodos
print(animal.lstrip())  # remueve los espacios en blanco a la izquierda
print(animal.rstrip())  # remueve los espacios en blanco a la derecha
# busca el indice de la palabra introducida
print(animal.find("ef"))  # regresa -1 si no encuentra nada
print(animal.replace("fE", "Je"))  # Reempleza una cadena por otra
# Devuelve un boleano para saber si existe o no una cadena de caracteres
print("cer" in animal)
print("cer" not in animal)
