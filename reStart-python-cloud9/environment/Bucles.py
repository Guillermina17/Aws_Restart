import random #importamos el modulo o la bibloteca random, para tener mas funciones para este lab

print("Bienvenido/a a el juego de adivinar el numero!")
print("Las reglas son sencillas. Yo pensare en un numero y tu trataras de adivinarlo.")

number = random.randint(1,10) #Funcion que permite generar un numero random, se guarda en la variable number
isGuessRight = False

while isGuessRight != True: #Mientras la variable isGuessRight sea distinta a True se ejecuta el loop
    guess =input("Adivina un numero entre 1 y 10: ")
    if int(guess)== number: #Si el numero que intenta adivinar el usuario (guess) es igual al numero que genero la funcion random, gana y cambia true isGuessRight
        print("Usted dijo el número {}. Esto es correcto! Tu ganas!".format(guess))
        isGuessRight = True
    else:
        print("Usted dijo el numero {}. Lo siento, no es correcto, intentalo de nuevo.".format(guess))   #Si el usuario no adivina el bucle sigue hasta que lo logre
        

