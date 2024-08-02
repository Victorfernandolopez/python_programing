import os
os.system('cls')

"""
Ejercicio 1
Sumar números con una función
Crear una función que tome 2 números como
argumentos y retorne el resultado.
Por ejemplo, el siguiente código:
sumar(10,30)
debe retornar:
40
"""
#declaracion de la funcion
def sumar(numeroA, numeroB):
    return numeroA+numeroB

#declaracion de la bariable
numero1 = 10
numero2 = 30

#mostrar el resultado de lo resuelto por la funcion suma
print(sumar(numero1,numero2))