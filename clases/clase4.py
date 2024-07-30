"""BUCLES EN PYTHON"""

# En Python, los bucles se utilizan para ejecutar un bloque de código repetidamente. Los dos tipos principales de bucles son `for` y `while`.

# BUCLE FOR
# El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena).

# Ejemplo básico de bucle for:
for i in range(5):
    print(i)  # Imprime los números del 0 al 4

# Explicación:
# `range(5)` genera una secuencia de números del 0 al 4.
# `i` toma cada valor de la secuencia en cada iteración del bucle.
# `print(i)` imprime el valor actual de `i`.

# Iterando sobre una lista:
mi_lista = [1, 2, 3, 4, 5]
for elemento in mi_lista:
    print(elemento)  # Imprime cada elemento de la lista

# Iterando sobre una cadena:
mi_cadena = "Hola"
for caracter in mi_cadena:
    print(caracter)  # Imprime cada carácter de la cadena

# BUCLE WHILE
# El bucle `while` se utiliza para repetir un bloque de código mientras una condición sea verdadera.

# Ejemplo básico de bucle while:
contador = 0
while contador < 5:
    print(contador)  # Imprime los números del 0 al 4
    contador += 1  # Incrementa el contador en 1

# Explicación:
# `contador` se inicializa en 0.
# El bucle `while` se ejecuta mientras `contador` sea menor que 5.
# `print(contador)` imprime el valor actual de `contador`.
# `contador += 1` incrementa el valor de `contador` en 1 en cada iteración.

# USO DE BREAK Y CONTINUE
# `break` se utiliza para salir de un bucle antes de que haya terminado normalmente.
# `continue` se utiliza para saltar el resto del código dentro del bucle y pasar a la siguiente iteración.

# Ejemplo de uso de break:
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es igual a 5
    print(i)  # Imprime los números del 0 al 4

# Ejemplo de uso de continue:
for i in range(10):
    if i % 2 == 0:
        continue  # Salta a la siguiente iteración si i es par
    print(i)  # Imprime los números impares del 0 al 9

# BUCLES ANIDADOS
# Los bucles pueden ser anidados, es decir, un bucle dentro de otro bucle.

# Ejemplo de bucles anidados:
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")  # Imprime todas las combinaciones de i y j

# Explicación:
# El bucle externo itera sobre `i` de 0 a 2.
# El bucle interno itera sobre `j` de 0 a 2 para cada valor de `i`.
# `print(f"i={i}, j={j}")` imprime la combinación actual de `i` y `j`.

# BUCLES CON ELSE
# Los bucles `for` y `while` pueden tener una cláusula `else` que se ejecuta cuando el bucle termina normalmente (sin un `break`).

# Ejemplo de bucle for con else:
for i in range(5):
    print(i)
else:
    print("Bucle for terminado")  # Se ejecuta después de que el bucle for termina

# Ejemplo de bucle while con else:
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Bucle while terminado")  # Se ejecuta después de que el bucle while termina

"""DICCIONARIOS EN PYTHON"""
"""DICCIONARIOS EN PYTHON"""

# Un diccionario en Python es una colección desordenada de pares clave-valor. Cada clave es única y se utiliza para acceder a su valor correspondiente.

# Creación de un diccionario:
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Accediendo a valores:
print(mi_diccionario["nombre"])  # Imprime: Juan
print(mi_diccionario["edad"])    # Imprime: 30

# Agregando o actualizando un valor:
mi_diccionario["edad"] = 31  # Actualiza el valor de la clave "edad"
mi_diccionario["profesión"] = "Ingeniero"  # Agrega una nueva clave-valor
print(mi_diccionario)  # Imprime: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesión': 'Ingeniero'}

# Eliminando un par clave-valor:
del mi_diccionario["ciudad"]  # Elimina la clave "ciudad" y su valor
print(mi_diccionario)  # Imprime: {'nombre': 'Juan', 'edad': 31, 'profesión': 'Ingeniero'}

# Métodos útiles de diccionarios:
# Obtener todas las claves:
print(mi_diccionario.keys())  # Imprime: dict_keys(['nombre', 'edad', 'profesión'])

# Obtener todos los valores:
print(mi_diccionario.values())  # Imprime: dict_values(['Juan', 31, 'Ingeniero'])

# Obtener todos los pares clave-valor:
print(mi_diccionario.items())  # Imprime: dict_items([('nombre', 'Juan'), ('edad', 31), ('profesión', 'Ingeniero')])

# Iterando sobre un diccionario:
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
# Imprime:
# nombre: Juan
# edad: 31
# profesión: Ingeniero

# Comprobando si una clave existe en el diccionario:
if "nombre" in mi_diccionario:
    print("La clave 'nombre' existe en el diccionario")

# Obtener un valor con un valor predeterminado si la clave no existe:
print(mi_diccionario.get("ciudad", "No disponible"))  # Imprime: No disponible

# Limpiar el diccionario:
mi_diccionario.clear()  # Elimina todos los elementos del diccionario
print(mi_diccionario)  # Imprime: {}

#usar un diccionario para contar vocales en una cadena

cadena = "Hola, mundo!"
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for letra in cadena:
    if letra.lower() in vocales:
        vocales[letra.lower()] += 1
print(vocales)  # Imprime: {'a': 1, 'e': 1, 'i': 1, 'o': 2, 'u': 1}

#expliquemos cada línea del código anterior
# la variable vocales es un diccionario donde las claves son las vocales en minúscula y los valores son la cantidad de veces que se encuentra esa vocal en la cadena
# la línea for letra in cadena itera sobre cada letra de la cadena
# si la letra en minúscula está en el diccionario vocales, se incrementa su valor en 1

