# Desarrolla un programa, que nos sirva para gestionar nuestros contactos 
# (la información a gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico. 
# El programa tendrá un menú, con las siguientes opciones: añadir contacto, consultar contacto a partir de la clave, 
# consultar todos los contactos y eliminar contacto. Aprovecha lo que has aprendido hasta el momento 
# (diccionarios, funciones, procedimientos…).

# Creamos la lista en el programa principal para que todas las funciones la puedan usar como global
contactos = []
def addContact():
    dict = {}
    nombre = input("Dime el nombre: ")
    dict['Nombre'] = nombre
    ap1 = input("Dime el primer apellido: ")
    dict['Primer apellido'] = ap1
    ap2 = input("Dime el segundo apellido: ")
    dict['Segundo apellido'] = ap2
    telefono = int(input("Dime el teléfono: "))
    dict['Teléfono'] = telefono
    email = input("Dime el email: ")
    dict['Email'] = email
    contactos.append(dict)

# Función que consulta todos los contactos
def consultarTodos():
    return contactos

# Función que consulta contactos a través de su posición en la lista. El índice será el número clave que introduce el usuario
def consultarKey(clave):
    return contactos[clave]

def eliminarContactos(posicion):
    return contactos.pop(posicion)




# print("¿Que quieres hacer?:")
# menu = input("- Añadir contacto" \n 
#             "- Consultar por clave" \n
###################### claveUser = int(input("Dime el número clave del contacto que quieres consultar: ")) print(consultarKey(claveUser))
#             "- Consultar por todos" \n
#             "- Eliminar todos" \n
#             "- Salir")

