"""Uso de funciones para implementar un cifrado cesar, el cual es un metodo que toma letras de un mensaje
    y las desplaza un cierto numero de lugares en el alfabeto"""

#Función que duplica el alfabeto o el argumento que le des
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
#Mensaje que le va a pedir al usuario para cifrar    
def getMessage():
    stringToEncrypt = input("Por favor ingrese un mensaje para cifrar: ")
    return stringToEncrypt
    
#Es la distancia que las letras va a moverse en el diccionario cuantas posiciones nos vamos a desplazar entre el 1-25
def getCipherKey():
    shiftAmount = input( "Por favor, ingrese una llave (número entero entre 1-25): ")
    return shiftAmount

#Esta funcion encripta el mensaje    
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter) #El metodo find busca eñ caracter actual
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Mensaje Cifrado: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Mensaje Descifrado: {myDecryptedMessage}')
    
"""El print f es para darle formato, si nosotros queremos mostrar una variable y algun tipo de texto
   el formateo es una f'entre las comillas simples va la cadena y luego la variable """

runCaesarCipherProgram()


