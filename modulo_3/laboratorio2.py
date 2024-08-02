import os
os.system('cls')

"""
Ejercicio 1
Forzar el ingreso numérico.
Crear un programa que pida un número, verificar
que ese ingreso por input sea un número posible
de convertir a entero. En caso contrario volver a
pedir el ingreso.
"""
while True:
    numero = input("ingrese un numero entero: ")
    if numero.isdigit():
        break
    else:
        print("error. numero no valido.")
print("numero ingresado correctamente...")


