#importamos la libreria os para poder limpiar la consola desde el codigo y el menu quede mas agradable para el usuario
import os
os.system('cls')
"""
¿Qué es el proyecto integrador?
● Se desarrollará un proyecto a lo largo de todo el curso.
● Permite reafirmar los conocimientos adquiridos.
● Los ejercicios se realizarán en la clase junto al profesor/a

Una vez hecho esto, se debe hacer que el programa, al iniciar, pregunte cuál de las siguientes dos
operaciones se debe realizar: ingresar un
alumno o ver la lista de alumnos ingresados.
Un ejemplo de lo que debe aparecer en consola,
en una posible implementación, es lo siguiente:

consola:
ingrese el numero de la operacion que desea ejecutar:
1 - añadir un alumno a la lista.
2 - ver la lista de alumnos.
3 - salir.

Esto debe preguntarse infinitamente hasta que el
usuario escriba “3”. 

Etapa 1
Una universidad desea crear un programa para
contabilizar los cursos que tiene cada alumno.
Para ello se debe realizar primero una aplicación
de consola la cual debe solicitar el nombre de un
alumno y la cantidad de cursos en la que se
encuentra inscripto.
Estos dos valores deben almacenarse como una
lista de dos elementos (el nombre y la cantidad
de cursos como un número entero) en una lista
de alumnos.

"""

#creacion de la lista donde se almacenaran los alumnos
alumnos = []
#creacion del menu
while True:
    print("ingrese el numero de la operacion que desea ejecutar: ")
    print("1 - añadir un alumno a la lista.")
    print("2 - ver la lista de alumnos.")
    print("3 - salir.")
    opcion = int(input())
    os.system('cls')
    #control de opciones
    if opcion == 1:
        print("AGREGAR ALUMNOS")
        nombre = input("ingrese el nombre: ")
        cursos = int(input("ingrese la cantidad de cursos: "))
        alumnos.append([nombre,cursos])
        print("has ingresado el alumno correctamente")
        os.system('pause')
        os.system('cls')
    elif opcion == 2:
        for alumno in alumnos:
            nombre = alumno[0]
            curso = alumno[1]
            print("LISTA DE ALUMNOS")
            print(f"nombre: {nombre}, cursos: {curso}")
        print("\n")
        os.system('pause')
        os.system('cls')
    elif opcion == 3:
        break
    else:
        print("la opcion ingresada no es la correcta, vuelva a intentarlo.")
print("gracias por utilizar el programa!")



