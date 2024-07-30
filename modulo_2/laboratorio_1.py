"""
Ejercicio 1
Comparar la entrada del usuario
Crear un programa que permita ingresar dos
cadenas vía la consola y luego las compare,
imprimiendo un mensaje en caso que sean
iguales y otro en caso que sean diferentes.
"""
#solicitar datos al usuario
cadena_1 = input("Ingrese la primer cadena: ")

cadena_2 = input("Ingrese la segunda cadena: ")

#comparar las cadenas

if cadena_1 == cadena_2:
    print("Las cadenas ingresadas son iguales")
else:
    print("Las cadenas ingresadas son diferentes")


"""
Ejercicio 2
Pedir nombre
Crear un programa que solicite el nombre de un
alumno a través de la consola, y luego chequee
que no esté vacío.
En caso de estarlo, tiene que imprimir un mensaje
de error; caso contrario, deberá imprimir un mensaje indicando que se ingresó correctamente.
"""

# Solicitar el nombre del alumno
nombre = input("Ingrese el nombre del alumno: ")

# Verificar que la cadena no esté vacía
if nombre:
    print("El nombre se ingresó correctamente.")
else:
    print("Error: No se ingresó ningún nombre.")


"""
Ejercicio 3
Comparar entrada de números
Pedir la edad por teclado y comparar si es
mayor o menor de edad. No olvidar de que para
poder comparar el ingreso debe ser convertido a
int, ya que el usuario ingresa un número entero.
"""

#solictar la edad del usuario

edad = int(input("Ingrese su edad: "))

#comparar la edad 

if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")


"""
Ejercicio 4
Dado un número entero, imprimir si es par o impar.
Pedir el número al usuario y convertirlo a entero.
"""

#solicitar el número al usuario y convertirlo a entero

numero = int(input("ingrese un numero: "))

#comparar si es par o inpar

if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")


"""
Ejercicio 5
Pedir un número al usuario y verificar si es un número primo.
Un número primo es un número natural que tiene exactamente dos divisores: 1 y el mismo número.
Nota: Para verificar si un número es primo, se debe comprobar si es divisible por todos los números menores que él mismo.
"""

#solicitar datos al usuario
numero = int(input("ingrese un numero: "))

#comprobar si el número es primo

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f"{numero} no es un numero primo")
            break
    else:
        print(f"{numero} es un numero primo")



"""
explicacion del for para comprovar si un número es primo:
    # empesamos comprovando si el numero ingresado es mayor que 1
        if numero > 1:

    # el rango empieza desde 2 y termina en el número ingresado (excluyendo ese número)
        if numero > 1:
            for i in range(2, numero):

    # el operador % nos permite obtener el residuo de la division entre el número y el número iterado en el for (i)
        if numero > 1:
            for i in range(2, numero):
                if (numero % i) == 0:

    # si el residuo es 0, significa que el número no es divisible solo por 1 y por ese número, por lo tanto no es primo y se sale del for con break
        if numero > 1:
            for i in range(2, numero):
                if (numero % i) == 0:
                    print(f"{numero} no es un numero primo")
                    break

    # si el for no se ejecuta el break, significa que no hay ningún número que divide al número ingresado, por lo tanto es primo. pasa a ejecutarse el else imprimiendo el mensaje de que el numero analizado es primo.
        if numero > 1:
            for i in range(2, numero):
                if (numero % i) == 0:
                    print(f"{numero} no es un numero primo")
                    break
            else:
                print(f"{numero} es un numero primo")
"""

