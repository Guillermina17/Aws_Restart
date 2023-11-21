miCadena = "Esto es una cadena guardada en una variable"
print(miCadena)
print(type(miCadena))
print(miCadena +". El tipo de dato es " + str(type(miCadena)))

cadena1 = "Cas"
cadena2 = "cada"
cadena3 = cadena1 + cadena2
print(cadena3)

nombre = input("¿Cuál es tu nombre? ")
print("Hola " + nombre + ", bienvenida a AWS re/start")

color =input("¿Cuál es tu color favorito? ")
animal = input("¿Cuál es tu animal fvorito? ")
print("{}, te gusta un {} {}!" .format(nombre,animal,color))

