# David ramírez - NÚMEROS PRIMOS

# Funcióin bucle "for" que valora si un número es primo o no.
# Recibe un parámetro y lo usa para determinar si es un número primo a través de divisiones.
# Retorna TRUE en el caso de ser primo, y FALSE en caso de no serlo   
def primosFor(numero):
    cont = 0
    for i in range(2, numero):
        resul = numero % i
        if resul == 0:
            cont += 1

    if cont >= 1:
        return False
    else:
        return True

# Función bucle "while" que valora si un número es primo o no.
# Recibe un parámetro y lo usa para determinar si es un número primo a través de divisiones.
# Retorna TRUE en el caso de ser primo, y FALSE en caso de no serlo   
def primosWhile(numero):
    i = 2
    cont = 0
    while i < numero:
        resul = numero % i
        if resul != 0:
            i += 1
        elif resul == 0:
            cont += 1
            i += 1
    
    if cont >= 1:
        return False
    else:
        return True

# Variables para guardar los valores del usuario
tipoBucle = input("Elige si quieres hacerlo con 'for' o 'while': ")
num = int(input("Escribe un número: "))

# Condicional que determina si el usuario elige hacer el cálculo con bucles "for" o "while".
# Dentro del condicional general contramos otro "if" para llamar a la función y así imprimir la respuesta según sea TRUE o FALSE.
if tipoBucle == "for":
    if primosFor(num):
        print(f"El número {num} es primo")
    else:
        print(f"El número {num} no es primo")

elif tipoBucle == "while":
    if primosWhile(num):
        print(f"El número {num} es primo")
    else:
        print(f"El número {num} no es primo")
else:
    print("Reinicia y escribe únicamente 'for' o 'while' por favor")