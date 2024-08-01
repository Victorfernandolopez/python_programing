import os
import math

#funcion para calcular el area de un circulo
def calcular_area_circulo(radio):
    return math.pi * radio**2
#ejemplo de uso

radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
print(f"El area del circulo es: {area}")

#calcular numeros primos hasta un numero dado

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

#ejemplo de uso

numero = int(input("Ingrese un numero: "))
if es_primo(numero):
    print(f"{numero} es un numero primo")
else:
    print(f"{numero} no es un numero primo")

#invertir una palabra

def invertir_palabra(palabra):
    return palabra[::-1]

#ejemplo de uso

palabra = input("Ingrese una palabra: ")
invertido = invertir_palabra(palabra)
print(f"La palabra invertida es: {invertido}")

"""juego de la memoria"""

import random
import time
# Función para mostrar la secuencia de números al usuario
def mostrar_secuencia(secuencia):
    print("Recuerda la secuencia de números: ")
    # Convierte la lista de números en una cadena y la imprime
    print(''.join(map(str, secuencia)))
    # Pausa la ejecución durante 2 segundos
    time.sleep(2)
    # Limpia la consola (compatible con Windows y Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para generar una lista de números aleatorios
def obtener_numero(longitud):
    # Genera una lista de números aleatorios de longitud especificada
    return [random.randint(0, 11) for _ in range(longitud)]

# Función principal del juego de memoria
def juego_de_memoria():
    # Inicializa la longitud de la secuencia y el puntaje
    longitud = 3
    puntaje = 0
    
    print("¡Bienvenido al juego de memoria!")
    while True:
        # Genera una secuencia de números aleatorios
        secuencia = obtener_numero(longitud)
        # Muestra la secuencia al usuario
        mostrar_secuencia(secuencia)
        # Pide al usuario que ingrese la secuencia
        respuesta = input("Ingresa la secuencia de números: ")
        # Convierte la respuesta del usuario en una lista de enteros
        respuesta_lista = [int(x) for x in respuesta]
        
        # Compara la secuencia ingresada con la generada
        if respuesta_lista == secuencia:
            print("¡Correcto!")
            # Incrementa el puntaje y la longitud de la secuencia
            puntaje += 1
            longitud += 1
        else:
            # Muestra la secuencia correcta y el puntaje
            print("Incorrecto, la secuencia era: ", secuencia)
            print("Tu puntaje es: ", puntaje)
            break

# Llama a la función principal para iniciar el juego
juego_de_memoria()


os.system('pause')
os.system('cls')