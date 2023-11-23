#Ejercicio 2: Al ejecutar una función, se pide ingresar una frase cualquiera y debe dar como resultado el conteo de caracteres.

def contador ():
    frase = input("Ingrese una frase cualquiera: ")
    cuenta = len(frase)
    
    print(f"La cantidad de caracters de la frase '{frase}' es: {cuenta}")
    return cuenta

contador()
