
"""
Etapa 2
La lista de alumnos que creamos en el módulo
anterior ahora debe ser un diccionario, en donde
las claves serán nombres de alumnos y los
valores sus respectivas cantidades de cursos.
Para esto se debe modificar el código de las
opciones 1 y 2 (agregar un nuevo alumno y ver la
lista de alumnos).
La tercera opción será “Ver la cantidad de cursos
de un alumno”. Deberá solicitar el nombre de un
alumno e imprimir en pantalla el número de
cursos que tiene asociados como clave. La cuarta
opción es la de salir, como en la versión anterior.
Usar todo lo aprendido hasta el momento, el
programa no debe de frenar de forma imprevista
a causa de un error. Ya que en el material de
lectura se vieron todas las posibles soluciones
frente a los problemas que se puedan presentar. 
"""
import os

#funcion para limpiar la pantalla
def limpiar_pantalla():
    os.system('pause')
    os.system('cls' if os.name == 'nt' else 'clear')

#funcion para mostrar el listado del menu
def imprimir_menu():
    print("ingrese el numero de la operacion que desea ejecutar: ")
    print("1 - añadir un alumno a la lista.")
    print("2 - ver la lista de alumnos.")
    print("3 - ver cantiad de  cursos por alumno")
    print("4 - salir.")

#funcion para agregar alumnos
def agregar_alumnos():
    print("AGREGAR ALUMNOS")
    nombre = input("ingrese el nombre: ")
    while True:
        cursos = input("ingrese la cantidad de cursos: ")
        if cursos.isdigit():
            cursos = int(cursos)
            alumnos[nombre] = cursos
            print("has ingresado el alumno correctamente")
            break
        else:
            print("Error. deve ingresar los cursos solo con digitos.")

#funcion para listar los alumnos
def listar_alumnos():
    print("LISTA DE ALUMNOS")
    if alumnos:
        for nombre, cursos in alumnos.items():
            print(f"Nombre: {nombre}, Cursos: {cursos}")
    else:
        print("No hay alumnos en la lista.")
    print("\n")

#funcion para ver cursos de por alumno
def ver_cantCursos():
    print("VER CURSOS POR ALUMNOS")
    while True:
        nombre = input("ingrese el nombre del alumno: ")
        if nombre in alumnos:
            print(f"El alumno {nombre} tiene {alumnos[nombre]} cursos")
            break
        else:
            print("Error, el alumno que busca no se encuentra en la lista de alumnos")

#programa principal

alumnos = {}
#creacion del menu
while True:
    imprimir_menu()
    opcion =input()
    #control de opciones
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            agregar_alumnos()
            limpiar_pantalla()
        elif opcion == 2:
            listar_alumnos()
            limpiar_pantalla()
        elif opcion == 3:
            ver_cantCursos()
            limpiar_pantalla()
        elif opcion == 4:
            break
        else:
            print("la opcion ingresada no es la correcta, vuelva a intentarlo.")
            limpiar_pantalla()
    else:
        print("Error. deve ingresar un digito correspondiente al digito de la opcion del menu a la que desea ingresar")
        limpiar_pantalla()
print("gracias por utilizar el programa!")

#nota: he mejorado el codigo a comparacion con el de la primera etapa, colocando cada bloque del menu en una funcion, y controlando todos los ingresos de teclado para que el programa no se cierre abruptamente y entregue un mensaje claro al usuario si lo ingresado no es lo que se esperaba