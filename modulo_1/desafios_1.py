"""
Ejercicio 1
Tomás rindió 3 exámenes, se desea saber su
promedio sabiendo que:
nota_uno = 10
nota_dos = 6
nota_tres = 8
Mostrar el promedio por pantalla.
"""
print("ejercicio 1")
nota_uno = 10
nota_dos = 6
nota_tres = 8

#promedio
print(f"promedio: {(nota_uno + nota_dos + nota_tres)/3}")


"""
Ejercicio 2
Hacer un programa que determine si una
persona es menor de edad o mayor de edad,
teniendo la edad en una variable.
Probar el código cambiando el valor de la
variable “edad”.
"""
print("ejercicio 2")

edad = 10
if edad > 17:
    print("es mayor de edad")
else:
    print("es menor de edad")


"""
Ejercicio 3
Un empleado cobró 300 dólares por mes desde enero
a junio, 500 dólares de julio a octubre, y 700 dólares
por mes en noviembre y en diciembre.
Hace un programa que calcule el sueldo promedio. Y
que diga si este “empleado” está cobrando un sueldo
bajo, normal o mejor de lo normal.
● Sueldo bajo: por debajo de 300 dólares.
● Sueldo normal: entre 300 a 900.
● Sueldo mejor de lo normal: más de 900 dólares.
"""
print("ejercicio 3")

enero_Junio = 300 * 6
julio_octubre = 500 * 4
noviembre_Diciembre = 700 * 2
sueldo_Promedio = (enero_Junio + julio_octubre + noviembre_Diciembre)/12
print(f"sueldo promedio: {sueldo_Promedio}")