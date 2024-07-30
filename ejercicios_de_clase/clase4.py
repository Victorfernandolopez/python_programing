"""EJERCICIOS"""

"1-suma de numeros pares"

suma = 0
for numero in range(101):
    if numero % 2 == 0:
        suma += numero

print(f"la suma total de los numeros pares del 0 al 100 es: {suma}")

"2-mostrar la tabla de multiplicar del 7"
tabla = 7
for num in range(11):
    print(f"{tabla} x {num} = {tabla*num}")

"3-conteo de vocales"
#pedir frase al usuario
frase = input("ingrese una frase: ").lower()

#mostrar la frase por pantalla
print(f"frase ingresada: '{frase}' ")

#pedir la vocal a contar
vocal = input("ingrese la vocal que desea contar: ").lower()

#mostrar la vocal seleccionada
print(f"la vocal seleccionada para contar es: {vocal}")

#contar cuantas veces aparece la vocal
contador = 0
for vocales in frase:
    if vocal == vocales:
        contador += 1

#mostrar cuantas veces se encontro la vocal en la frase
print(f"se encontro {contador} veces la vocal en la frase: {frase}")

#ejemplo 2 usando un diccionario

cadena = "Hola, mundo!"
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for letra in cadena:
    if letra.lower() in vocales:
        vocales[letra.lower()] += 1
print(vocales)  # Imprime: {'a': 1, 'e': 1, 'i': 1, 'o': 2, 'u': 1}

"4-promedio de una lista"
lista = [10,9,5,7,98]
suma = 0
for valor in lista:
    suma += valor
promedio = suma / len(lista)
print(f"el promedio de la lista[10,9,5,7,98] es: {promedio}")

"5- adivina el numero secreto"
#importamos la libreria random
import random

#declaramos las variables
numero_secreto = random.randint(1, 10)
intentos = 0
vidas = 3

#bucle del juego

while intentos < vidas:
    #solicitar el numero al usuario
    numero_usuario = int(input("Adivina el numero secreto (1-10): "))
    #incrementar el numero de intentos
    intentos += 1
    #comparar el numero ingresado con el numero secreto
    if numero_usuario == numero_secreto:
        print("Felicidades! Adivinaste el numero secreto.")
        break
    elif numero_usuario < numero_secreto:
        print("El numero ingresado es menor al numero secreto.")
    else:
        print("El numero ingresado es mayor al numero secreto.")
    #restar una vida si el numero ingresado no es el correcto
    #mostrar el numero de vidas restantes
    print(f"Te quedan {vidas-intentos} vidas.")
else:
    print("Perdiste! El numero secreto era:", numero_secreto)

"6-secuencia de fibonacci"

limite = int(input("Ingrese el limite de la secuencia de Fibonacci: "))
a,b = 0, 1
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b

"7- cuenta regresiva con patrones"

for i in range(10, 0, -1):
    for j in range(5,i-1, -1):
        print(j, end="")


