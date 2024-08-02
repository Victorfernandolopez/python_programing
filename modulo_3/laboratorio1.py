import os
os.system('cls')
"""
Ejercicio 1
Múltiplos
Se quiere buscar los múltiplos de 3 y de 5 en un
rango que ingrese el usuario. Guardar los
múltiplos en una lista.
Se debe usar for asociado a un range como se
vio en la teoría.
"""
rango = int(input("ingrese el limite de busqueda de multiplos de 3 y 5: "))
multiplos_3 = []
multiplos_5 = []
for i in range(1,rango + 1):
    if i % 3 == 0:
        multiplos_3.append(i)
    if i % 5 == 0:
        multiplos_5.append(i)
print("los multiplos de 3 son: ")
print(multiplos_3)
print("los multiplos de 5 son: ")
print(multiplos_5)











