# range define el rango de datos que se van a recorrer con el for
# la variable que definimos, tomara el valor que corresponda al range
# for numero in range(5):
#     print(numero)

# break permite terminar con la ejecución del codigo
buscar = 5
for numero in range(5):
    print(numero)
    if numero == buscar:
        print('Encontrado:', buscar)
        break
else:  # se acompaña con un else para definir el caso de que no se cumpla la condición
    print('No encontre el numero :(')

# tambien se pueden iterar string
for char in "Ultimate Python":
    print(char)
