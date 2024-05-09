# cuando se le pasan dos ** al parametro, se debe definir el nombre del datos cuando se pase el parametro
def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="4", name="Raul", desc="test")
