# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2

# comando = ""

# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)

# para hacer un loop infinito, debemos especificar siempre un metodo de salida
while True:
    comando = input("$ ")
    print(comando)
    if comando == "salir":
        break
