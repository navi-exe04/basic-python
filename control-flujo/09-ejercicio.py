print("Bienvenido a la calculadora.")
print("Para salir, escribe el comando \"salir\"")

resultado = 0

while True:
    if not resultado:
        resultado = input('Ingrese un numero: ')
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    opcion = input(
        "Ingresa una operacion (sumar, restar, multiplicar, dividir): ")
    if opcion.lower() == "salir":
        break

    numero2 = input("Ingresa otro numero: ")
    if numero2.lower() == "salir":
        break
    numero2 = int(numero2)

    if opcion.lower() == "sumar":
        resultado += numero2
    elif opcion.lower() == "restar":
        resultado -= numero2
    elif opcion.lower() == "multiplicar":
        resultado *= numero2
    elif opcion.lower() == "dividir":
        resultado /= numero2
    else:
        print("Operacion no valida")

    print(f"Resultado de la operacion: {resultado}")
