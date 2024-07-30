"""entrada y convercion de datos"""

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

"""
explicacion del codigo:
1.
nombre = input("Ingrese su nombre: ")
Esta línea solicita al usuario que ingrese su nombre. La función input() muestra el mensaje "Ingrese su nombre: " en la consola y espera a que el usuario escriba algo y presione Enter.
Lo que el usuario escribe se almacena en la variable nombre.
2.
print(f"Hola {nombre}!")
Esta línea imprime un saludo en la consola.
Utiliza una f-string (cadena formateada) para incluir el valor de la variable nombre dentro del mensaje. Las f-strings se indican con una f antes de las comillas y permiten insertar variables directamente dentro de las llaves {}.
El resultado es que si el usuario ingresó, por ejemplo, "Juan", la salida será: Hola Juan!.
"""

edad = int(input("Ingrese su edad: "))
anio_actual = 2024
anio_nacimiento = anio_actual - edad
print(f"Usted nacio en el año {anio_nacimiento}")

"""
1.
edad = int(input("Ingrese su edad: "))
Esta línea solicita al usuario que ingrese su edad. La función input() muestra el mensaje "Ingrese su edad: " en la consola y espera a que el usuario escriba algo y presione Enter.
Lo que el usuario escribe se captura como una cadena de texto (string). La función int() convierte esa cadena en un número entero.
El valor resultante se almacena en la variable edad.
2.
anio_actual = 2024
Esta línea asigna el valor 2024 a la variable anio_actual. Esto representa el año actual.
3.
anio_nacimiento = anio_actual - edad
Aquí se calcula el año de nacimiento del usuario restando su edad del año actual.
El resultado de esta operación se almacena en la variable anio_nacimiento.
4.
print(f"Usted nacio en el año {anio_nacimiento}")
Esta línea imprime un mensaje en la consola.
Utiliza una f-string (cadena formateada) para incluir el valor de la variable anio_nacimiento dentro del mensaje.
El resultado es que si, por ejemplo, el usuario ingresó que tiene 30 años, la salida será: "Usted nacio en el año 1994"."""

peso = float(input("Ingrese su peso en kilogramos: "))
print(f"Usted pesa {peso} kilogramos")

#-----------------------------------------------------------------------------------------------

"""LISTAS, TUPLAS, SETS, MATRICES"""

"""DEFINICIONES DE LISTAS"""
"""
Una lista en Python es una colección ordenada y mutable de elementos. Los elementos de una lista pueden ser de diferentes tipos (números, cadenas, otros objetos, etc.). Las listas se definen utilizando corchetes [] y los elementos se separan por comas.

Ejemplo de una lista:
mi_lista = [1, 2, 3, "cuatro", 5.0]

CARACTERISTICAS:
Las características principales de las listas en Python son:

1.
Ordenadas: Los elementos en una lista tienen un orden definido y este orden no cambia a menos que se modifique explícitamente.
2.
Mutables: Los elementos de una lista pueden ser cambiados, es decir, se pueden agregar, eliminar o modificar elementos después de que la lista ha sido creada.
3.
Permiten duplicados: Las listas pueden contener elementos duplicados, es decir, el mismo valor puede aparecer más de una vez en una lista.
4.
Indexadas: Los elementos de una lista pueden ser accedidos mediante índices, donde el primer elemento tiene el índice 0, el segundo el índice 1, y así sucesivamente.
5.
Heterogéneas: Una lista puede contener elementos de diferentes tipos de datos, como enteros, cadenas, flotantes, e incluso otras listas.
6.
Dinámicas: Las listas pueden cambiar de tamaño automáticamente, es decir, pueden crecer o reducirse según se agreguen o eliminen elementos.
"""

# EJEMPLO DE USO DE LISTAS

mi_lista = [1, 2, 3, "cuatro", 5.0]
print(mi_lista)  # Imprime: [1, 2, 3, "cuatro", 5.0]

mi_lista.append("cinco")  # Agrega un elemento al final de la lista
print(mi_lista)  # Imprime: [1, 2, 3, "cuatro", 5.0, "cinco"]

mi_lista.insert(2, "uno")  # Inserta un elemento en un índice específico

print(mi_lista)  # Imprime: [1, 2, "uno", 3, "cuatro", 5.0, "cinco"]

mi_lista.remove("uno")  # Elimina el primer elemento que coincida con el valor especificado

print(mi_lista)  # Imprime: [1, 2, 3, "cuatro", 5.0, "cinco"] 

del mi_lista[1]  # Elimina el elemento en el índice especificado

print(mi_lista)  # Imprime: [1, 3, "cuatro", 5.0, "cinco"] 

# ACCEDIENDO A LOS ELEMENTOS DE UNA LISTA

print(mi_lista[0])  # Imprime: 1
print(mi_lista[2])  # Imprime: 3
print(mi_lista[-1])  # Imprime: "cinco"

# BUSCANDO UN ELEMENTO EN UNA LISTA

print(1 in mi_lista)  # Imprime: True
print("uno" in mi_lista)  # Imprime: False

# CONTANDO EL NUMERO DE VECES QUE APARECE UN ELEMENTO EN UNA LISTA

print(mi_lista.count("cinco"))  # Imprime: 1

# ORDENANDO UNA LISTA

mi_lista.sort()  # Ordena la lista en orden ascendente
print(mi_lista)  # Imprime: [1, 3, "cuatro", 5.0, "cinco"]

mi_lista.reverse()  # Invierte la lista
print(mi_lista)  # Imprime: ["cinco", 5.0, "cuatro", 3, 1] 

# CONCATENANDO UNA LISTA CON OTRA

otro_lista = ["seis", 7.0]
mi_lista += otro_lista  # Concatena la lista mi_lista con la otro_lista
print(mi_lista)  # Imprime: [1, 3, "cuatro", 5.0, "cinco", "seis", 7.0]

# DEVOLVIENDO UNA SUBLISTA 

sub_lista = mi_lista[2:5]  # Devuelve una sub lista desde el índice 2 hasta el índice 4 (excluyente)
print(sub_lista)  # Imprime: ["cuatro", 5.0, "cinco"]

# ELIMINANDO UNA SUBLISTA

del mi_lista[2:5]  # Elimina una sub lista desde el índice 2 hasta el índice 4 (excluyente)
print(mi_lista)  # Imprime: [1, 3, "seis", 7.0]


"""DEFINICIONES DE TUPLAS"""

"""
Una tupla en Python es una colección ordenada e inmutable de elementos. Los elementos de una tupla pueden ser de diferentes tipos (números, cadenas, otros objetos, etc.). Las tuplas se definen utilizando paréntesis () y los elementos se separan por comas.

Ejemplo de una tupla:
mi_tupla = (1, 2, 3, "cuatro", 5.0)
"""

"""CARACTERISTICAS:
Las características principales de las tuplas en Python son:

1.
Ordenadas: Los elementos en una tupla tienen un orden definido y este orden no cambia.
2.
Inmutables: Una vez que una tupla ha sido creada, no se pueden cambiar, agregar o eliminar elementos. Esto significa que las tuplas son inmutables.
3.
Permiten duplicados: Las tuplas pueden contener elementos duplicados, es decir, el mismo valor puede aparecer más de una vez en una tupla.
4.
Indexadas: Los elementos de una tupla pueden ser accedidos mediante índices, donde el primer elemento tiene el índice 0, el segundo el índice 1, y así sucesivamente.
5.
Heterogéneas: Una tupla puede contener elementos de diferentes tipos de datos, como enteros, cadenas, flotantes, e incluso otras tuplas.
"""

# EJEMPLO DE USO DE TUPLAS

mi_tupla = (1, 2, 3, "cuatro", 5.0)
print(mi_tupla)  # Imprime: (1, 2, 3, "cuatro", 5.0)

# ACCEDIENDO A LOS ELEMENTOS DE UNA TUPLA

print(mi_tupla[0])  # Imprime: 1
print(mi_tupla[2])  # Imprime: 3
print(mi_tupla[-1])  # Imprime: 5.0

# BUSCANDO UN ELEMENTO EN UNA TUPLA

print(1 in mi_tupla)  # Imprime: True
print("uno" in mi_tupla)  # Imprime: False

# CONTANDO EL NUMERO DE VECES QUE APARECE UN ELEMENTO EN UNA TUPLA

print(mi_tupla.count("cuatro"))  # Imprime: 1

# CONCATENANDO UNA TUPLA CON OTRA

otro_tupla = ("seis", 7.0)
mi_tupla += otro_tupla  # Concatena la tupla mi_tupla con la otro_tupla
print(mi_tupla)  # Imprime: (1, 2, 3, "cuatro", 5.0, "seis", 7.0)

# DEVOLVIENDO UNA SUBTUPLA

sub_tupla = mi_tupla[2:5]  # Devuelve una sub tupla desde el índice 2 hasta el índice 4 (excluyente)
print(sub_tupla)  # Imprime: (3, "cuatro", 5.0)

# ELIMINANDO UNA SUBTUPLA

del mi_tupla[2:5]  # Elimina una sub tupla desde el índice 2 hasta el índice 4 (excluyente)
print(mi_tupla)  # Imprime: (1, 2, "seis", 7.0)

"""DEFINICIONES DE SETS"""

"""
Un set en Python es una colección desordenada de elementos únicos. Los sets se definen utilizando llaves {} o la función set(). Los elementos de un set no tienen un orden específico y no se permiten duplicados.

Ejemplo de un set:
mi_set = {1, 2, 3, "cuatro", 5.0}

CARACTERISTICAS:
Las características principales de los sets en Python son:

1.
Desordenados: Los elementos en un set no tienen un orden definido.
2.
Elementos únicos: Un set no puede contener elementos duplicados.
3.
Mutables: Los sets pueden ser modificados, es decir, se pueden agregar o eliminar elementos después de que el set ha sido creado.
4.
No indexados: Los elementos de un set no pueden ser accedidos mediante índices, ya que no tienen un orden específico.
5.
Heterogéneos: Un set puede contener elementos de diferentes tipos de datos, como enteros, cadenas, flotantes, e incluso otros sets.
"""

"""EJEMPLO DE USO DE SETS"""

mi_set = {1, 2, 3, "cuatro", 5.0}
print(mi_set)  # Imprime: {1, 2, 3, "cuatro", 5.0} 

# AGREGANDO ELEMENTOS A UN SET

mi_set.add("cinco")  # Agrega un elemento al set
print(mi_set)  # Imprime: {1, 2, 3, "cuatro", 5.0, "cinco"}

# ELIMINANDO ELEMENTOS DE UN SET

mi_set.remove("cuatro")  # Elimina un elemento del set
print(mi_set)  # Imprime: {1, 2, 3, 5.0, "cinco"}

# CHECANDO SI UN ELEMENTO EXISTE EN UN SET

print(1 in mi_set)  # Imprime: True
print("uno" in mi_set)  # Imprime: False

# UNION DE SETS

otro_set = {4, 5, 6, "seis"}
union_set = mi_set.union(otro_set)  # Unión de los sets
print(union_set)  # Imprime: {1, 2, 3, 4, 5, 6, 5.0, "cinco", "seis"}

# INTERSECCION DE SETS

interseccion_set = mi_set.intersection(otro_set)  # Intersección de los sets
print(interseccion_set)  # Imprime: {5}

# DIFERENCIA DE SETS

diferencia_set = mi_set.difference(otro_set)  # Diferencia entre los sets
print(diferencia_set)  # Imprime: {1, 2, 3, 4, 5.0, "cinco"}

# DISJOIN DE SETS

disjoint_set = mi_set.isdisjoint(otro_set)  # Verifica si los sets son disjointos
print(disjoint_set)  # Imprime: False

# CONTANDO EL NUMERO DE ELEMENTOS DE UN SET

print(len(mi_set))  # Imprime: 6

# REMOVENDO TODOS LOS ELEMENTOS DE UN SET

mi_set.clear()  # Remueve todos los elementos del set
print(mi_set)  # Imprime: set()

# COPIANDO UN SET

otro_set = mi_set.copy()  # Copia los elementos de un set
print(otro_set)  # Imprime: {1, 2, 3, 4, 5.0, "cinco"}

# ELIMINANDO UN SET ENTERO

del mi_set  # Elimina el set
print(mi_set)  # Imprime: NameError: name'mi_set' is not defined



"""DEFINICIONES DE MATRICES"""

"""
Una matriz en Python es una colección bidimensional de elementos, organizada en filas y columnas. Las matrices se pueden representar utilizando listas anidadas, donde cada sublista representa una fila de la matriz.

Ejemplo de una matriz:
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

CARACTERISTICAS:
Las características principales de las matrices en Python son:

1.
Bidimensionales: Las matrices tienen dos dimensiones, filas y columnas.
2.
Ordenadas: Los elementos en una matriz tienen un orden definido basado en su posición en filas y columnas.
3.
Mutables: Los elementos de una matriz pueden ser cambiados, es decir, se pueden agregar, eliminar o modificar elementos después de que la matriz ha sido creada.
4.
Indexadas: Los elementos de una matriz pueden ser accedidos mediante índices de fila y columna.
5.
Heterogéneas: Una matriz puede contener elementos de diferentes tipos de datos, aunque generalmente se utilizan elementos del mismo tipo para mantener la consistencia.
"""

"""EJEMPLO DE USO DE MATRICES"""

mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(mi_matriz)  # Imprime: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# AGREGANDO FILAS A UNA MATRIZ

mi_matriz.append([10, 11, 12])  # Agrega una fila al final de la matriz
print(mi_matriz)  # Imprime: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# AGREGANDO COLUMNAS A UNA MATRIZ

for fila in mi_matriz:
    fila.append(0)  # Agrega un 0 al final de cada fila de la matriz
print(mi_matriz)  # Imprime: [[1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0], [10, 11, 12, 0]]
#nota: recorreremos cada fila de la matriz para agregar el 0 al final 

# ELIMINANDO FILAS Y COLUMNAS 


del mi_matriz[1]  # Elimina la fila en la posición 1
print(mi_matriz)  # Imprime: [[1,2,3,0],[7,8,9,0],[10,11,12]
del mi_matriz[0][1]  # Elimina el elemento en la posición (0, 1)
print(mi_matriz)  # Imprime: [[1,3,0],[7,8,9,0],[10,11,12,0]]

# CONTANDO EL NUMERO DE FILAS Y COLUMNAS DE UNA MATRIZ

print(len(mi_matriz))  # Imprime: 3
print(len(mi_matriz[0]))  # Imprime: 3

# COPIANDO UNA MATRIZ

otro_matriz = mi_matriz.copy()  # Copia los elementos de una matriz
print(otro_matriz)  # Imprime: [[3, 0], [7, 0], [10, 0], [11, 0], [12, 0]]

# REMOVIENDO TODOS LOS ELEMENTOS DE UNA MATRIZ

mi_matriz.clear()  # Remueve todos los elementos de la matriz
print(mi_matriz)  # Imprime: []

# ELIMINANDO UNA MATRIZ ENTERA

del mi_matriz  # Elimina la matriz
print(mi_matriz)  # Imprime: NameError: name 'mi_matriz' is not defined
