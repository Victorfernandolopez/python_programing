"""
Ejercicio 1
Acceso a una matriz
Los conceptos que se deberán emplear para
resolver estos ejercicios son: listas, bucle while
y bucle for, la palabra reservada break,
condicionales, la instrucción input, la instrucción int para convertir una cadena a un número
entero y str para convertir un número a una
cadena, el operador + para concatenar dos o
más cadenas, y cualquier otra que nos sea útil
para este propósito
"""

"""
1. Crear un programa que solicite una fila y una
columna e imprima en pantalla el número en
esa posición según la siguiente matriz:
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
Un ejemplo de entrada (lo que escribe el
usuario) y salida (lo que se imprime en
pantalla) es el siguiente (los caracteres
en azul son ingresados por el usuario):
Fila: 1
Columna: 2
6.4
El resultado es 6.4 puesto que es el valor
ubicado en matriz[1][2].
"""
"""
2. El programa debe chequear que la fila y la
columna tengan valores válidos.
En este caso, las únicas filas válidas son 0 y 1;
las columnas, 0, 1 y 2. Si alguno de los dos
valores es inválido, debe mostrar un mensaje
de error.
"""
matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]

print("dada la siguiente matriz")
print("[3.3, 6.1, 4.0]")
print("[4.9, 5.7, 6.4]")
print("seleccionar algun valor, ingresando el valor de la fila (1 o 2) y el valor de la columna (1,2 o 3)")

fila = ""
columna = ""

#pedir fila y comprovar que sea un valor valido
while not fila:
    fila = int(input("\ningrese el valor de la fila: "))
    if fila>0 and fila<3:
        break
    else:
        print(f"\nerror... {fila} no es un valor valido")
        print("ingrese un valor entre 1 y 2")
        fila = ""

print(f"la fila seleccionada es {fila}")

#pedir columna y comprovar que sea un valor valido
while not columna:
    columna = int(input("\ningrese el valor de la columna: "))
    if columna>0 and columna<4:
        break
    else:
        print(f"\nerror... {columna} no es un valor valido")
        print("ingrese un valor entre 1 y 3")
        columna = ""

print(f"la columna seleccionada es {columna}")

#imprimir el valr de la posicion seleccionada
print(f"el valor seleccionado es: {matriz[fila-1][columna-1]}")