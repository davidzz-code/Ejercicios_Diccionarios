# David Ramírez - AGENDA DE CONTACTOS

# Creamos la lista en el programa principal para que todas las funciones la puedan usar como global
contactos = []

# Función que añade los contactos a la lista.
# Cada elemento de la lista es un diccionario distinto 
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
def consultarKey(claveParam):
    return contactos[claveParam]

# Función que borra el contacto a través de su posición en la lista
def eliminarContactos(posicionParam):
    return contactos.pop(posicionParam)



print("Bienvenido/a a la agenda, ¿que operación quieres realizar?:")
menu = input("- Añadir contacto \n- Consultar por clave \n- Consultar todos \n- Eliminar contacto \n- Salir \nOpción: ")

# Bucle while que llama a las distintas funciones según la elección del usuario.
while menu != "Salir":
    if menu == "Añadir contacto":
        addContact()
        print("Añadido con éxito")
        menu = input("- Añadir contacto \n- Consultar por clave \n- Consultar todos \n- Eliminar contacto \n- Salir \nOpción: ")
    elif menu == "Consultar por clave":
        claveVar = int(input("Dime el la posición en la agenda del contacto que quieres consultar: ")) 
        print(consultarKey(claveVar))
        menu = input("- Añadir contacto \n- Consultar por clave \n- Consultar todos \n- Eliminar contacto \n- Salir \nOpción: ")
    elif menu == "Consultar todos":
        print(f"Estos son todos los contactos: {consultarTodos()}")
        menu = input("- Añadir contacto \n- Consultar por clave \n- Consultar todos \n- Eliminar contacto \n- Salir \n Opción: ")
    elif menu == "Eliminar contacto":
        posicionVar = int(input("Dime el la posición en la agenda del contacto que quieres eliminar: ")) 
        print(f"Has eliminado a: {eliminarContactos(posicionVar)}")
        menu = input("- Añadir contacto \n- Consultar por clave \n- Consultar todos \n- Eliminar contacto \n- Salir \nOpción: ")
    else:
        menu = input("..:Esa opción no existe, por favor elige una opción:.. : \n- Añadir contacto \n- Consultar por clave \n- Consultar todos \n- Eliminar contacto \n- Salir \nOpción: ")