nombre_curso = "Ultimate Python"

# las triples comillas permite establecer una cadena de texto que ocupe varias lineas
# de igual forma se pueden usar para definir documentacion del software (se puede usar sin asignar a una variable)
descripcion_curso = """
Ultimate Python
este curso contempla todos los detalles
que necesitas aprender para encontrar
un trabajo como programador.
"""

print(nombre_curso, descripcion_curso)

# len permite saber el tamaño de un string
print(len(nombre_curso))
# podemos acceder a cualquier caracter de la cadena con []
print(nombre_curso[0])
# podemos cortar un string con : definiendo el inicio y final de la cadena
print(nombre_curso[0:8])
print(nombre_curso[9:])
