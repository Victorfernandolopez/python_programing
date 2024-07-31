"""
Ejercicio 1
Incrementar una variable
Con un bucle while incrementar una variable
entera de uno en uno (desde 0 a 10 sin incluir).
Mostrar por pantalla el resultado por vuelta.
"""

#declaracion de variables
a = 0

#incrementar la variable a hasta 9
while a < 10:
    #mostrar el resultado por vueltas
    print(f"a = {a}")
    #incrementar valor de a
    a += 1
else:
    print("fin del bucle")


"""
Ejercicio 2
Volver a pedir
Pedir por teclado el nombre de usuario, si
está vacío, volver a pedirlo hasta que se ingrese
un nombre.
Luego, saludar al usuario
"""
#inicializacion de la variable nombre vacia
nombre = ""

#solicitar un nombre hasta que se ingrese algun texto
#nota: sabiendo que el bucle while se ejecuta siempre que la condicion sea verdadera vamos a negar el valor de la variable nombre, con el objetivo de que el bucle se repita hasta contener algo, cuando esto suceda, al verificar la condicion ya con la variable con contenido, la condicion se volvera FALSE y saldra del bucle

while not nombre:
    nombre = input("ingrese su nombre: ")
else:
    print("fin del siclo")
