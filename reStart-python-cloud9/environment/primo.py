import math
primos = []
for numero in range(1, 251):
    divisor = int(math.sqrt(numero))
    n = 0
    for x in range(1 , divisor + 1):
        if numero % x == 0:
            n += 1
    if n < 2:
        primos.append(numero)


with open ("primos.txt", "w") as f:
    for i in primos:
        f.write(str(i)+", ")