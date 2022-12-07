# David Ramírez - CONTAR PALABRAS

# Variable que guarda la frase del usuario
fraseUsuario = str(input("Escribe una frase y contaré las palabras: "))

################################################# A. Asumimos que cada palabra está separada por un solo espacio en blanco #############################################

def contarPalabras_V1(frase):
    # Determina el número de palabras a través del bucle "for" guardando los espacios en blanco en una variable
    palabras = 1
    for i in frase:
        if i == " ":
            palabras += 1

    return palabras

################################################# B. No sabemos como están separadas las palabras #############################################

# El bucle "for" recorre la frase del usuario y compara con la variable "signos".
# En caso de encontrar algún signo de puntuación, añadirá un guión 
def contarPalabras_V2(frase):
    lista = []
    signos = " ,;.:-_/~#¿?¡!<>}{[]*"
    for i in frase:
        if i in signos:
            lista.append("-")
        else:
            lista.append(i)
        nuevaFrase = "".join(lista)
    
    fraseFinal = nuevaFrase.split("-")
    
    # Borra los guiones de la lista de manera que únicamente nos queda una lista de palabras y basta con retornar la longitud de la lista 
    while "" in fraseFinal:
        fraseFinal.remove("")
        
    return len(fraseFinal)


print(f"SOLO ESPACIOS EN BLANCO:")
print(f"En la frase hay: {contarPalabras_V1(fraseUsuario)} palabras")
print()

print(f"DISTINTOS CARÁCTERES:")
print(f"En la frase hay: {contarPalabras_V2(fraseUsuario)} palabras")