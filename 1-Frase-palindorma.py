# David Ramírez - FRASE PALÍNDROMA

# La función comprueba a través de un "if" si la cadena de texto coincide al leerla de derecha a izquierda y viceversa.
def comprobarFrase(frase):
    textoNuevo = frase.replace(" ", "")

    if textoNuevo == textoNuevo[::-1]:
        return "La frase es palíndroma"
    else:
        return "La frase no es palíndroma"

# Variable que guarda la variable del usuario
fraseUsuario = input("Escribe una frase: ")

# Imprime el resultado pasando la frase del usuario como parámetro
print(comprobarFrase(fraseUsuario))