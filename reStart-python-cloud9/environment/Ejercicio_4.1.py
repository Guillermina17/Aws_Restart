#Ejercicio 4:Crear función donde elegir entre suma, resta, multiplicación, división y efectuar cálculo de dos valores ingresados.

def operaciones(a,b):
    operacion = input("¿Que operacion desea realizar? Escriba: Suma, Resta, Multiplicacion o Division: ")
    if operacion == "Suma" or operacion == "suma":
        sumar = a + b
        print(f"La suma dio: {sumar}")
        return sumar
        
    elif operacion == "Resta" or operacion == "resta":
        restar = a-b
        print(f"La resta dio: {restar}")
        return restar
        
    elif operacion == "Multiplicacion" or operacion == "multiplicacion":
        multiplica = a*b
        print(f"La multiplicación dio: {multiplica}")
        return multiplica
        
    elif operacion == "Division" or operacion == "division":
        divi = a/b
        print(f"La división dio: {divi}")
        return divi
        
    else:
        print("Error, eso no es una operación realizable")
        
prueba = operaciones(10,5)



