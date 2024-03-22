# Leer un numero natural para evaluar la condicion
numero = int(input("Ingrese un número natural: "))

# Definir una primera condicion
if 0 > numero:
    print("El numero " + str(numero) + "no es un numero natural")

# Definir la otra condicion para hallar el factorial del numero natural ingresado
else:
    factorial = 1
    i = 1
    while numero >= i:
        factorial *= i
        i += 1
    print("El factorial de " + str(numero) + " es " +str(factorial))
