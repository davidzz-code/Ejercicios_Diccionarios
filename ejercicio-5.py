# Desarrolla un programa, que nos sirva para gestionar nuestros contactos 
# (la información a gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico. 
# El programa tendrá un menú, con las siguientes opciones: añadir contacto, consultar contacto a partir de la clave, 
# consultar todos los contactos y eliminar contacto. Aprovecha lo que has aprendido hasta el momento 
# (diccionarios, funciones, procedimientos…).

contactos = {}
lista = []


def addContact():
    i = 1
    nombre = input("Dime el nombre: ")
    lista.append(nombre)
    ap1 = input("Dime el primer apellido: ")
    lista.append(ap1)
    ap2 = input("Dime el segundo apellido: ")
    lista.append(ap2)
    telefono = int(input("Dime el teléfono: "))
    lista.append(telefono)
    email = input("Dime el email: ")
    lista.append(email)
    contactos[i] = lista
    i += 1
    return contactos

print(addContact())




