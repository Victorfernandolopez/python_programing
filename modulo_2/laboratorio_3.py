"""
Ejercicio 1
Lista de nombres
Se tiene la siguiente lista de nombres:
nombres = ["Susana","Alejandro","Roberto"]
Insertar entre Alejandro y Roberto a Paula. Y luego
agregar al final a Silvina.
Para finalizar, hay que recorrer la lista y mostrar a
todos los nombres por pantalla.
"""
nombres = ["Susana","Alejandro","Roberto"]

#insertar entre alejandro y roberto a paula
nombres.insert(2,"paula")
print(nombres)

#agregar al final de la lista a silvina
nombres.append("silvina")
print(nombres)

