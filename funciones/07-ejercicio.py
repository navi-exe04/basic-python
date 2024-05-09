def borrar_espacios(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def invertir_texto(texto):
    texto_invertido = ""
    for char in texto:
        texto_invertido = char + texto_invertido
    return texto_invertido


def es_palindromo(texto):
    texto = borrar_espacios(texto).lower()
    texto_invertido = invertir_texto(texto)

    return texto == texto_invertido


print(es_palindromo("Anita lava la tina"))
print(es_palindromo("Hola mundo"))
