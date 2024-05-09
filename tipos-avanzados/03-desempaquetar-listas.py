numeros = [1, 2, 3]

# podemos obtener los valores por separado de la lista de la siguiente forma
primero, segundo, tecero = numeros
print(primero, segundo, tecero)

# tambien podemos obtener el primer y ultimo valor de la siguiente forma
primero, *otros, ultimo = numeros
print(primero, otros, ultimo)
