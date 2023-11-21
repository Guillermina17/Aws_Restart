contestacion =input("Necesitas enviar el paquete? (escribe sí o no) ")
if contestacion == "si":
    print("Podemos ayudarte a enviar ese paquete")
else:
    print("Por favor, vuelve cuando necesites enviar un paquete. Gracias.")
    

user = input("Le gustaria comprar sellos, un sobre o una copia? (Escribe sello, sobre o copia) ")
if user == "sello":
    print("Tenemos muchos sellos para ofrecerle")
elif user == "sobre":
    print("Tenemos una variedad de sobres")
elif user == "copia":
    copias = input("Cuantas copias le gustaría tener? (Escribe un numero) ")
    print("Aqui tiene {} copias, que tenga un buen día.".format(copias))
else:
    print("Muchas gracias, por favor vuelve pronto")