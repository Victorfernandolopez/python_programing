"""funciones - parametros args y kwargs"""

'explicación de la función y cómo se utilizan los parámetros args y kwargs en Python'

"""args: es una tupla que contiene todos los argumentos de entrada que no están en el diccionario kwargs. Cada elemento de la tupla es un argumento independiente. El uso de args es útil cuando se necesita pasar un número arbitrario de argument datos a una función. Por ejemplo, la función `sum_numbers(*args)` puede recibir cualquier número de argumentos enteros y retornar la suma de todos ellos. args puede ser vacío si no se pasan argumentos adicionales. Por ejemplo:
    def sum_numbers(*args):
        total = 0
        for num in args:
            total += num
        return total
    print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15  # Se pasan varios argumentos enteros a la función sum_numbers y el resultado es 15 (1+2+3+4+5)."""

"""kwargs: es un diccionario que contiene todos los argumentos de entrada  que están en el diccionario kwargs. Cada par clave-valor en el dic kwargs es un argumento de entrada independiente. El uso de kwargs es útil cuando se necesita pasar un número arbitrario de argumentos de entrada con nombre y valor a una función. Por ejemplo, la función `print_arguments(**kwargs)` puede recibir cual quier número de argumentos de entrada con nombre y valor y imprimirlos en pantalla como pares clave-valor. kwargs puede ser vacío si no se pasan argumentos adicionales con nombre y valor. Por ejemplo:
    def print_arguments(**kwargs):
    for key, value in kwargs.items():
    print(f"{key}: {value}")
"""
def suma(*args):
    return sum(args)

print(suma(1, 2, 3, 4, 5))

def print_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_arguments(nombre="Juan", edad=30, profesion="Programador")

def producto(*args):
    producto = 1
    for num in args:
        producto *= num
    return producto
print(producto(1,2, 3, 4))

#maximo

def maximo(*args):
    return max(args)
print(maximo(1, 2, 3, 4, 5))

#minimo 

def minimo(*args):
    return min(args)
print(minimo(1, 2, 3, 4, 5))

#suma_pares

def suma_pares(*args):
    suma = 0
    for num in args:
        if num % 2 == 0:
            suma += num

print(suma_pares(1, 2, 3, 4, 5))

#suma_impares

def suma_impares(*args):
    suma = 0
    for num in args:
        if num % 2 != 0:
            suma += num

print(suma_impares(1, 2, 3, 4, 5))

#promedio

def promedio(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(promedio(1, 2, 3, 4, 5))

def elementos_unicos(*args):
    return list(set(args))#set elimina los duplicados y convierte a lista

print(elementos_unicos(1, 2, 3, 2, 1, 4, 5, 5))

def filtrar_pares(*args):
    return [num for num in args if num % 2 == 0] #list comprehension para generar una lista con los pares de los argumentos de entrada 

"""LISTAS COMPREHENSIONS: Una lista comprensión es una forma compacta de crear una lista a partir de una lista o cualquier otro tipo de iterable. La lista comprensión se escribe en una sola línea y utiliza la sintaxis de corchetes. Los elementos de la lista se generan utilizando una expresión que puede incluir operaciones aritméticas, llamadas a funciones, y expresiones booleanas. La lista comprensión se puede utilizar para filtrar, transformar, o combinar elementos de una lista. Por ejemplo:
pares = [num for num in [1, 2, 3, 4, 5] if num % 2 == 0]  # Output: [2, 4]  # Se crea una lista con los pares de los números en la lista original."""

#ejemplos de kwargs

def imprimir_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

imprimir_kwargs(nombre="Juan", edad=30, profesion="Programador")

def imprimir_kwargs_con_formato(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.upper()}: {value}")

imprimir_kwargs_con_formato(nombre="Juan", edad=30, profesion="Programador")

def imprimir_kwargs_con_formato_y_ordenado(**kwargs):
    kwargs = dict(sorted(kwargs.items(), key=lambda item: item[0]))  # Ordena los pares clave-valor por la clave
    for key, value in kwargs.items():
        print(f"{key.upper()}: {value}")

imprimir_kwargs_con_formato_y_ordenado(nombre="Juan", edad=30, profesion="Programador")

def sumar_kwargs(**kwargs):
    return sum(kwargs.values())

print(sumar_kwargs(a=1, b=2, c=3))  # Output: 6  # Se suman todos los valores de los pares clave-valor en kwargs

def multiplicar_kwargs(**kwargs):
    producto = 1
    for value in kwargs.values():
        producto *= value
    return producto

print(multiplicar_kwargs(a=2, b=3, c=4))  # Output: 24  # Se multiplica todos los valores de los pares clave-valor en kwargs

def concatenar_kwargs(**kwargs):
    return "".join(kwargs.values())

print(concatenar_kwargs(a="H", b="e", c="l", d="l", e="o"))  # Output: Hello  # Se concatena todos los valores de los pares clave-valor en kwargs

def generar_kwargs(**kwargs):
    return kwargs

print(generar_kwargs(a=1, b=2, c=3))  # Output: {'a': 1, 'b': 2, 'c': 3}  # Se devuelve un nuevo diccionario con los pares clave-valor en kwargs

def filtrar_kwargs_pares(**kwargs):
    return {key: value for key, value in kwargs.items() if value % 2 == 0}  # Se crea un nuevo diccionario con los pares clave-valor en kwargs que son pares

print(filtrar_kwargs_pares(a=1, b=2, c=3, d=4, e=5))  # Output: {'b': 2, 'd': 4}  # Se filtran los pares clave-valor en kwargs que son pares

def filtrar_kwargs_impares(**kwargs):
    return {key: value for key, value in kwargs.items() if value % 2 != 0}  # Se crea un nuevo diccionario con los pares clave-valor en kwargs que son impares

print(filtrar_kwargs_impares(a=1, b=2, c=3, d=4, e=5))  # Output: {'a': 1, 'c': 3, 'e': 5}  # Se filtran los pares clave-valor en kwargs que son impares

def filtrar_kwargs_por_valor_minimo(**kwargs):
    min_value = min(kwargs.values())
    return {key: value for key, value in kwargs.items() if value == min_value}  # Se crea un nuevo diccionario con los pares clave-valor en kwargs que tienen el valor mínimo

print(filtrar_kwargs_por_valor_minimo(a=1, b=2, c=3, d=2, e=1))  # Output: {'a': 1, 'e': 1}  # Se filtran los pares clave-valor en kwargs que tienen el valor mínimo

def filtrar_kwargs_por_valor_maximo(**kwargs):
    max_value = max(kwargs.values())
    return {key: value for key, value in kwargs.items() if value == max_value}  # Se crea un nuevo diccionario con los pares clave-valor en kwargs que tienen el valor máximo

print(filtrar_kwargs_por_valor_maximo(a=1, b=2, c=3, d=2, e=1))  # Output: {'b': 2}  # Se filtran los pares clave-valor en kwargs que tienen el valor máximo

"""LIBRERIAS"""

#TKINTER: Librería para crear interfaces gráficas de usuario (GUI) en Python

#CREAR UNA VENTANA EMERJENTE
import tkinter as tk
from tkinter import messagebox


def mostrar_mensage():
    messagebox.showinfo("hola chicos", "Hola mundo!")

#crear ventana
root = tk.Tk()
root.withdraw() #ocultar la ventana

#mostrar el mensaje emergente
mostrar_mensage()

root.mainloop()

import arcade

#constante
screen_width = 800
screen_height = 600
screen_title = "Mi primer juego"
movement_speed = 5

class persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

class estudiannte(persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    def estudiar(self):
        print(f"Estudio en la carrera de {self.carrera}.")

persona1 = persona("Juan", 30)
persona1.saludar()

estudiante1 = estudiannte("Ana", 25, "Ingeniería en Sistemas")