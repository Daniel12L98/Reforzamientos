import Problema_05

def main():
    nombre = input("Ingrese su nombre de usuario: ")
    result = Problema_05.validar_nombre(nombre)
    if result is True:
        print("Nombre de usuario válido.")
    else:
        print("Error:", result)

if __name__ == "__main__":
    main()