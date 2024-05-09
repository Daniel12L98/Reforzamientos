def funcion():
    try:
        persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
        indice = persona['profesion']
        return indice
    except KeyError:
        raise KeyError("La palabra 'profesión' no se encuentra en el diccionario")
try:
    profesion = funcion()
    print("El la profesión de la persona es:", profesion)
except KeyError as e:
    print(e)
