diccionario = {}
diccionario["uno"] = 1
diccionario["dos"] = 2
diccionario[3] = "tres"
diccionario["cuatro"] = 4.4

print(diccionario[3])


for key, value in diccionario.items():
    print(key,value)