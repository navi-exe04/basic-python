# el * antes del nombre del parametro, permite definir que es un dato iterable
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(2, 3, 4, 5)
suma(1)
