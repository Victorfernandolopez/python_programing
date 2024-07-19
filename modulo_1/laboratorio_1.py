"""
Ejercicio 1
Sumar tres variables
En un script de Python, crear tres variables
nombradas a, b y c con valores numéricos
cualesquiera; una cuarta llamada resultado que
sea la suma de las primeras tres, y por último
imprimir en pantalla cada una de ellas.
Antes de mostrar el valor de cada variable,
indicar su nombre en una línea anterior.
"""
print("ejercicio 1")
#creacion de las variables
a = 5
b = 7
c = 10

#suma de las variables
resultado = a + b + c

#imprecion de las variables
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"resultado: {resultado}")

print("ejercicio 2")

"""
Ejercicio 2
Concatenar dos cadenas
Crear dos variables, saludo y nombre, cuyos
contenidos sean "Hola, " en el primer caso y tu
nombre en el segundo. Intenta sumarlas vía el
operador + y mostrar el resultado en pantalla.
Para guardar el resultado de la suma puedes
crear una tercera variable.
"""
#CREACION DE VARIABLES
saludo = "hola"
nombre = "victor"

#concatenacion con +
concatenacion = saludo +" "+ nombre
print(concatenacion)

#concatenar separando con comas
print(saludo,nombre)

#concatenar con comas y sustituirlas por cualquier otro simbolo
print(saludo,nombre, sep="***")