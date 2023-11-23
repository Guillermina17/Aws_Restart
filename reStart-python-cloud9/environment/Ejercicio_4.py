#Ejercicio 4:Crear función donde elegir entre suma, resta, multiplicación, división y efectuar cálculo de dos valores ingresados.

def suma(a,b):
    sumar = a + b
    return sumar

def resta(a,b):
    restar = a-b
    return restar

def multiplicación (a,b):
    multiplica = a*b
    return multiplica

def division (a,b):
    divi = a/b
    return divi

suma_1 = suma(5,17)
print(f"La suma dio: {suma_1}")

resta_1 = resta(10,5)
print(f"La resta dio: {resta_1}")

multiplicacion_1 = multiplicación(5,10)
print(f"La multiplicacion dio: {multiplicacion_1}")

division_1 = division (15,3)
print(f"La division dio: {division_1}")




    