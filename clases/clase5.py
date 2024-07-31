"""MATRICES EN PYTHON"""

"""
son listas de listas que permiten almacenar múltiples valores en una sola una variable.
se accede a cada elemento de una matriz mediante dos índices, uno para la fila y otro para la columna.
"""

# Ejemplos de matrices en Python:
matriz = [[1, 2, 3], [4, 5, 6]]  # Matriz de dos filas y tres columnas

#operaciones con matrices
suma_elementos =  matriz[0][0] + matriz[0][1] + matriz [0][2] + matriz[1][0] + matriz[1][1 ] + matriz[1][2] # Suma de todos los elementos de la matriz
print("Suma de todos los elementos de la matriz:", suma_elementos)

#suma recorriendo la matriz con un bucle
suma_elementos_b = 0
for fila in matriz:
    for elemento in fila:
        suma_elementos_b += elemento # Suma de todos los elementos de la matriz
print("Suma de todos los elementos de la matriz con bucle:", suma_elementos_b)

"""DICCIONARIOS EN PYTHON"""

"""
son colecciones de pares de valores, donde cada par consiste de una clave (key) y un valor (value).
las claves deben ser únicas dentro de un diccionario y pueden ser de cualquier tipo de dato.
Los valores pueden ser de cualquier tipo de dato, incluyendo otros diccionarios.
"""

# Ejemplos de diccionarios en Python:
diccionario = {"nombre": "Juan", "apellido": "Pérez", "edad": 30}

# Acceso a los valores del diccionario
nombre = diccionario["nombre"]
apellido = diccionario["apellido"]
edad = diccionario["edad"]

print("Nombre:", nombre)
print("Apellido:", apellido)
print("Edad:", edad)

# Modificando los valores del diccionario
diccionario["apellido"] = "Gómez"
print("Apellido modificado:", diccionario["apellido"])

# Añadiendo nuevos pares clave-valor
diccionario["direccion"] = "Calle 123"
print("Dirección:", diccionario["direccion"])

# Eliminando pares clave-valor
del diccionario["direccion"]
print("Dirección eliminada:", diccionario.get("direccion", "No se ha encontrado la clave"))

#recorriendo un diccionario con un bucle

for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

"""RANGES EN PYTHON"""

"""
son objetos iterables que generan secuencias de números.
se utilizan para realizar bucles, contar o iterar sobre secuencias de datos.
"""

# Ejemplos de ranges en Python:

# Rango de números desde 0 hasta 4 (exclusive)
range_1 = range(5)

# Rango de números desde 5 hasta 10 (exclusive)
range_2 = range(5, 10)

# Rango de números de 0 a 9 con saltos de 2
range_3 = range(0, 10, 2)

# Iterando sobre un range
for numero in range_1:
    print(numero)

for numero in range_2:
    print(numero)

for numero in range_3:
    print(numero)

# Rangos con float
range_4 = range(0.5, 5.0, 0.5)
for numero in range_4:
    print(numero)

# Rangos con cadenas
range_5 = range("A", "F")
for letra in range_5:
    print(letra)

# Rangos con objetos
class MiObjeto:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

range_6 = range(MiObjeto(1), MiObjeto(5))
for objeto in range_6:
    print(objeto)

"""ISDIGITS EN PYTHON"""

"""
son funciones incorporadas en Python que verifican si todos los caracteres en una cadena son dígitos.
"""

# Ejemplos de isdigits en Python:

# Verificando si todos los caracteres en una cadena son dígitos
cadena_1 = "12345"
print(cadena_1.isdigit())  # Imprime: True

cadena_2 = "123abc"
print(cadena_2.isdigit())  # Imprime: False

