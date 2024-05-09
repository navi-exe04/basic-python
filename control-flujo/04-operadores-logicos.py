# and, or, not

gas = False
encendido = True
edad = 18

if not gas and (encendido or edad > 17):
    print("Puedes avanzar")

# los operadores siempre se ejecutan de izquierda a derecha
# los operadores de corto circuito, permite interrumpir la ejecución
# de una instancia cuando cierta comparacion de false (en caso de que sea and)
# o regrese un true (en caso de que sea or)
# se recomienda no escribir los () cuando sea un operador de corto circuito
if not gas and encendido or edad > 17:
    print("Puedes avanzar")
