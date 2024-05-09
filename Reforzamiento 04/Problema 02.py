def funcion():
    try:
        lista = [2, 6, 10, 4, 5, 23, 1, 9, 9, 9]
        posicion = lista[10]
        return posicion
    except IndexError:
        raise IndexError("No existe valor en la posición indicada")
try:
    resultado = funcion()
    print("El valor en esa posición es:", resultado)
except IndexError as e:
    print(e)
