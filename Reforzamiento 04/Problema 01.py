def funcion():
    try:
        suma = 80 + "Hola Pythonistas"
        return suma
    except TypeError:
        raise TypeError("No es posible sumar un numero (int) con una cadena de caracteres (str)")
try:
    resultado = funcion()
    print("El resultado de la suma es:", resultado)
except TypeError as e:
    print(e)
