#ejercicio 1
#calcular el area de un rectangulo

#inicializar variables
base = 10
altura = 5

#calcular el area del rectangulo
area = base * altura
print(f"El area del rectangulo es: {area}")

# ejemplo 2
# calcular el area de un rectangulo con ingreso de datos
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

#calcular el area del rectangulo

area = base * altura
print(f"El area del rectangulo es: {area}")

# ejercicio 2
# convertir grados celsius a grados farenheit

grados_celsius = float(input("Ingrese los grados celsius: "))

# formula para convertir grados celsius a grados farenheit
"""
Ten en cuenta que la ecuación es °F = (°C x 1,8) + 32. También puedes usar la ecuación °F = °C x 9 ÷ 5 + 32. Esta arrojará el mismo resultado, ya que 9 ÷ 5 = 1,8. Para convertir a grados Fahrenheit, puedes introducir cualquier temperatura Celsius en cualquiera de las ecuaciones mencionadas.
"""
grados_farenheit = (grados_celsius * 9/5) + 32
print(f"{grados_celsius} grados celsius son {grados_farenheit} grados farenheit")

#ejercicio 3
#calcular el area del circulo
#para calcular el area de un circulo, se utiliza la formula A = πr^2 (donde A es el area y r es el radio del circulo)

#importar la biblioteca math para utilizar la constante pi
import math

#ingreasar el radio del circulo
radio = float(input("Ingrese el radio del circulo: "))
#calcular el area del circulo
area = math.pi * radio**2
#mostrar el area del circulo
print(f"El area del circulo es: {area}")

#ejercicio 4
#verificar si un numero es par o impar

#ingrese un numero
numero = int(input("Ingrese un numero: "))
#verificar si el numero es par o impar utilizando el operador modulo (%) para obtener el resto de la division entera
es_par = numero % 2 == 0

#mostrar el resultado
if es_par:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

#ejercicio 5
#verificar si un numero es positivo, negativo o cero

#ingrese un numero
numero = int(input("Ingrese un numero: "))

#verificar si el numero es positivo, negativo o cero utilizando el operador comparativo
if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero")

#ejercicio 6: verificar si un estudiante aprobó un examen

#solicitar la nota del estudiante
nota = int(input("Ingrese la nota del estudiante: "))
#verificar si el estudiante aprobó el examen utilizando el operador booleano
aprobado = (nota >= 7)
#mostrar el resultado
print(f"El estudiante aprobo el examen: {aprobado}")

#ejercicio 7: verificar si un numero esta entre 10 y 90

#solicitar un numero al usuario
numero = int(input("Ingrese un numero: "))

#verificar si el numero esta entre 10 y 90 utilizando el operador booleano
comparacion = (numero >= 10) and (numero <= 90)

#mostrar el resultado
print(f"{numero} esta entre 10 y 90: {comparacion}")


#ejercicio 8: verificar si una cadena tiene la letra 'a' o 'e'

#solicitar una cadena al usuario
cadena = input("Ingrese una cadena: ")

#verificar si la cadena tiene la letra 'a' o 'e' utilizando el operador booleano
comparacion = ('a' in cadena.lower()) or ('e' in cadena.lower())

#mostrar el resultado
print(f"La cadena {cadena} contiene la letra 'a' o 'e': {comparacion}")

#CONDICIONALES

#teoria de condicionales
# if condicion:
    # bloque de codigo a ejecutar si la condicion es verdadera
# else:
    # bloque de codigo a ejecutar si la condicion es falsa

#ejercicio 9: verificar si un numero es positivo, negativo o cero 

#solicitar un numero al usuario
numero = int(input("Ingrese un numero: "))

#verificar si el numero es positivo, negativo o cero utilizando condicionales

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero")

#ejercicio 10: verificar si un año es visiesto o no
#Un año es bisiesto si es divisible por 4. Sin embargo, si el año es divisible por 100, no es bisiesto, a menos que también sea divisible por 400.

# solicitar un año al usuario
año = int(input("Ingrese un año: "))

# verificar si el año es bisiesto utilizando condicionales
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")

