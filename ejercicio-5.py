# Desarrolla un programa, que nos sirva para gestionar nuestros contactos 
# (la información a gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico. 
# El programa tendrá un menú, con las siguientes opciones: añadir contacto, consultar contacto a partir de la clave, 
# consultar todos los contactos y eliminar contacto. Aprovecha lo que has aprendido hasta el momento 
# (diccionarios, funciones, procedimientos…).

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

def consultarTodos():
    return contactos

print(consultarTodos())
# print(f"Estos son los contactos: {consultarTodos()}")
# def consultarKey(clave):
#     contactos.get("clave", "No existe")


# print("¿Que quieres hacer?:")
# menu = input("- Añadir contacto" \n 
#             "- Consultar por clave" \n
#             "- Consultar por todos" \n
#             "- Eliminar todos" )

