# David Ramírez - FECHA COMPLETA

# Creamos una variable tipo string ya que el usuario mezclará números con carácteres no numéricos
fechaUsuario = input("Dame una fecha en formato dd/mm/YYYY: ")

# Diccionario para relacionar los números con el nombre del mes
dict = {"01" : "Enero",
        "02" : "Febrero",
        "03" : "Marzo",
        "04" : "Abril",
        "05" : "Mayo",
        "06" : "Junio",
        "07" : "Julio",
        "08" : "Agosto",
        "09" : "Septiembre",
        "10" : "Octubre",
        "11" : "Noviembre",
        "12" : "Dicimbre"
}

# Procedimiento que separa el string por el símbolo "/" usando un "split" y creando así una lista
# Utilizando los índices accede a lista y al diccionario para imprimir el resultado por pantalla.
def fechaCompleta(fecha):
    lista = fecha.split("/")
    print(f"{lista[0]} de {dict[lista[1]]} de {lista[2]}")

# Llamada a la función con el parámetro de la variable con los datos que ha introducido el usuario
fechaCompleta(fechaUsuario)