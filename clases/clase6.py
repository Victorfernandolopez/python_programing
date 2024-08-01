import os

"""FUNCIONES"""

"""la funcion es un bloque de codigo que se ejecuta cuando se llama a esta función"""

#sintaxis de una función en Python
"""
def nombre_funcion(parametro1, parametro2):
    #cuerpo de la función
    return resultado  #el resultado de la función se devuelve al llamador
"""

#ejemplo de una funcion que suma dos numeros

def sumar(a, b):
    return a + b

"""AMBITO DE LAS VARIABLES"""

#variables locales y globales

#una variable local solo puede ser accedida dentro de su función
def sumar_con_variables_locales(a, b):
    suma = a + b  #variable local
    return suma

#una variable global puede ser accedida desde cualquier parte del programa
total = 0
def sumar_con_variables_globales(a, b):
    global total
    total += a + b  #variable global
    return total

"""libreria math"""
#importamos la libreria math
import math
"las funciones mas usadas de la libreria math son:"

print(math.sqrt(16))  #raiz cuadrada
print(math.factorial(5))  #factorial
print(math.pi)  #constante pi
print(math.sin(math.radians(90)))  #seno en grados
print(math.cos(math.radians(90)))  #coseno en grados
print(math.tan(math.radians(45)))  #tangente en grados








os.system('pause')
os.system('cls')