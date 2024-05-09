def validar_nombre(nombre):
    if len(nombre) < 7:
        return "El nombre de usuario debe contener al menos 7 caracteres"
    elif len(nombre) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    elif not nombre.isalnum():
        return "El nombre de usuario puede contener solo letras y números"
    else:
        return True