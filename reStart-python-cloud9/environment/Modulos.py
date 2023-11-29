import math
absoluto = -5.999
floor_test =198.42

resultado1 = math.fabs(absoluto)
resultado2 = math.floor(floor_test)

print (resultado1, " es el valor absoluto de ", absoluto)
print(resultado2, "es el flujo de: ", floor_test)

print("Aqui esta mi diario")
dia =open("environment/diario.txt", "r")
print(dia.read())



